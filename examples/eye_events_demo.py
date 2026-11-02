"""PC integration demo. Start mx_eye in Simulation mode first.

0 = animal entry, I = confirm RFID, Space = next target, L = leave, Esc = quit.
Uses real MXBI Flow detector forwarding and display-flip timestamps.
"""

from pathlib import Path
import argparse
import logging
import time
from threading import Thread

import pygame
from py_mx_eye import MxEye, MxEyeConfig

from mxbiflow import get_mxbiflow, set_base_path
from mxbiflow.driver import MXBI, MXBIModel
from mxbiflow.driver.detector import MockDetector
from mxbiflow.driver.detector.detector import DetectionResult
from mxbiflow.driver.eyetracker import MxEyeEyetracker
from mxbiflow.driver.rewarder import MockRewarder
from mxbiflow.gameloop.detector_bridge import DetectorBridge
from mxbiflow.gameloop.game import Game
from mxbiflow.models.animal import Animal, AnimalConfig, StageState
from mxbiflow.models.session import Session, SessionConfig, SessionState
from mxbiflow.scene import SceneManager
from mxbiflow.scene.scene import Scene


class DemoIdle(Scene):
    def start(self):
        self._running = True

    def quit(self):
        self._running = False

    def handle_event(self, event):
        pass

    def update(self, dt_s):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (45, 45, 45), screen.get_rect())


class EventTarget(DemoIdle):
    def start(self):
        super().start()
        self.index = 0
        self._show("stimulus_shown")

    def _show(self, kind):
        self.position = ((200, 300), (512, 150), (820, 450))[self.index]
        get_mxbiflow().stimulus_event(
            kind, "red-target", stimulus_type="circle",
            position=self.position, size=(40, 40), metadata={"target_index": self.index}
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.index = (self.index + 1) % 3
            self._show("stimulus_changed")

    def quit(self):
        get_mxbiflow().stimulus_event("stimulus_hidden", "red-target")
        super().quit()

    def draw(self, screen):
        pygame.draw.circle(screen, (230, 45, 45), self.position, 20)
        gaze = get_mxbiflow().eye_sample
        if gaze:
            pygame.draw.circle(screen, (255, 255, 255), (round(gaze.x), round(gaze.y)), 5)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke", action="store_true", help="automate the demo keys for a quick check")
    parser.add_argument("--control-port", type=int, default=5557)
    parser.add_argument("--data-port", type=int, default=5556)
    args = parser.parse_args()
    set_base_path(Path.cwd() / "eye_events_demo_data")
    config = AnimalConfig(name="demo_monkey", rfid_id="demo-rfid", stage="event_target")
    animal = Animal(config=config, current_stage_name=config.stage,
                    stages={config.stage: StageState(stage_name=config.stage)})
    session = Session(
        config=SessionConfig(animals=(config,), unknown_animal_as=config.name),
        mxbi_config=MXBIModel(mxbi_id="pc-demo"),
        state=SessionState(animals={config.name: animal}),
    )
    detector = MockDetector()
    tracker = MxEyeEyetracker(MxEye(MxEyeConfig(control_port=args.control_port, data_port=args.data_port)),
                              send_experiment_events=True, record_on_animal=True)
    mxbi = MXBI((1024, 600), MockRewarder(logging.getLogger("demo")), detector, tracker)
    bridge = DetectorBridge(detector, {config.rfid_id: config.name})
    manager = SceneManager()
    manager.register({"idle": DemoIdle, "event_target": EventTarget})
    manager.default_scene = "idle"
    game = Game(session, manager, bridge, mxbi)
    game._shortcuts.register(pygame.K_i, "Confirm RFID",
        lambda _: bridge._on_animal_identified(DetectionResult(animal_id="demo-rfid")))
    pygame.display.set_caption("MXBI events: 0 enter | I RFID | Space target | L leave | Esc quit")
    if args.smoke:
        def keys():
            for key in (pygame.K_0, pygame.K_i, pygame.K_SPACE, pygame.K_l, pygame.K_ESCAPE):
                time.sleep(0.6)
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=key))
        Thread(target=keys, daemon=True).start()
    game.play()


if __name__ == "__main__":
    main()
