"""Ordered, acknowledged experiment events without blocking Pygame."""

import json
import time
from pathlib import Path
from queue import Full, Queue
from threading import Thread

from py_mx_eye import ExperimentEvent, MxEye

from ..utils.logger import logger


class EyeEventSender:
    def __init__(self, client: MxEye, log_path: Path):
        self.client = client
        self.log_path = log_path
        self.error = ""
        self._queue: Queue[ExperimentEvent | None] = Queue(maxsize=1024)
        self._closed = False
        self._thread = Thread(target=self._work, name="mx-eye-events", daemon=True)
        self._thread.start()

    def send(self, event: ExperimentEvent) -> None:
        if self._closed:
            return
        try:
            self._queue.put_nowait(event)
        except Full:
            self.error = "mx-eye event queue full; event was not delivered"
            logger.error(self.error)

    def _work(self) -> None:
        try:
            self._deliver()
        except Exception as exc:
            self.error = f"mx-eye event sender stopped: {exc}"
            logger.error(self.error)

    def _deliver(self) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as log:
            while True:
                event = self._queue.get()
                try:
                    if event is None:
                        return
                    error = ""
                    status = None
                    for attempt in range(3):
                        try:
                            status = self.client.send_event(event)
                            error = ""
                            break
                        except Exception as exc:  # Delivery failure must not kill the game.
                            error = str(exc)
                            if attempt < 2:
                                time.sleep(0.2)
                    self.error = error
                    if error:
                        logger.error("mx-eye event delivery failed: %s", error)
                    log.write(json.dumps({
                        "event": event.model_dump(mode="json"),
                        "acknowledged": not bool(error),
                        "error": error,
                        "recording_directory": status.directory if status else None,
                    }) + "\n")
                    log.flush()
                finally:
                    self._queue.task_done()

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        # Shutdown may wait for acknowledgements; normal frame processing never does.
        self._queue.put(None)
        self._thread.join(timeout=65)
        if self._thread.is_alive():
            logger.error("mx-eye events still pending at shutdown; check eye_events.jsonl")
