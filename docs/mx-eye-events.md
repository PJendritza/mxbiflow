# MXBI Flow → mx_eye events (first PC implementation)

Work branches: `feature/mx-eye-events` in mxbiflow and `feature/mxbi-events`
in mx_eye. The framework base is 0.3.26 + the gaze-coordinate fix.

## Run on this PC

### Update another checkout for testing

Use both matching branches from PJendritza's repositories. In each existing
checkout, save any local edits before switching branches. These commands stop
on conflicting edits; do not discard those edits to proceed.

First update mx_eye (PowerShell, from its checkout):

```powershell
git fetch origin
git switch feature/mxbi-events
git pull --ff-only origin feature/mxbi-events
uv sync --all-extras
```

Then update mxbiflow (PowerShell, from its checkout). These commands assume the
two repositories are sibling folders, as on this PC:

```powershell
git fetch origin
git switch feature/mx-eye-events
git pull --ff-only origin feature/mx-eye-events
uv sync --locked
```

The MXBI Flow branch pins the matching MX Eye SDK, so no manual SDK installation
or special `--no-sync` launch command is required.

### Launch the demo

The matching protocol and SDK are installed by the normal `uv sync --locked`
command. No experiment dependencies or config files are changed by the demo.

PowerShell window 1:

```powershell
cd "C:\Users\patri\Code\mxbi\mx_eye"
uv run mx-eye
```

Select **Simulation**, press **Start**, and leave this window running. Its local
network settings must use bind `127.0.0.1`, data port 5556, control port 5557.

PowerShell window 2:

```powershell
cd "C:\Users\patri\Code\mxbi\mxbiflow"
uv run python examples/eye_events_demo.py
```

- `0`: animal enters; mx_eye starts a new recording.
- `I`: RFID identification event, in the same recording.
- `Space`: change the red target position.
- `L`: animal leaves; recording finalizes; tracking continues.
- `Esc`: close the task and finish the owned recording if still active.

Watch the **MXBI** line at the bottom of mx_eye and its Record button. The demo
uses MXBI Flow's real detector bridge, game loop and SDK transport. It uses mock
hardware and does not touch the existing experiment's config or data.

## Enable in an existing experiment

Install this mxbiflow branch in the experiment environment. A task that pins an
older mxbiflow commit cannot see this branch's framework changes.
Set these fields on the enabled `mx_eye` eyetracker in its `mxbi.json`:

```json
{"send_experiment_events": true, "record_on_animal": true}
```

Both default to false. Acquisition must already be running in mx_eye; this
feature controls recording, not acquisition. It refuses to take over a manual
recording. Allow recording to finish before the next visit.

Animal events are automatic. A task must explicitly describe its visual stimuli:

```python
get_mxbiflow().stimulus_event(
    "stimulus_shown", "target-1", stimulus_type="image",
    position=(512, 300), size=(100, 100), metadata={"image": "apple.png"},
)
```

Call once when updating what `draw()` will show. Use `stimulus_changed` for a
change, and `stimulus_hidden` when removing it. Coordinates use Pygame's screen
pixels. The game sends queued stimulus descriptions immediately after the next
display flip. This is a host presentation timestamp, not a measured photon
onset. Scene transitions now apply before drawing so newly started scenes are
actually drawn on the flip their onset describes. Avoid queuing contradictory
stimulus changes in a frame; describe the final displayed state.

## Saved data and transport

- The existing ZeroMQ REQ/REP command endpoint carries events and replies after
  saving them. The SDK exposes `send_event`, `start_recording`, `stop_recording`.
- A separate framework worker sends events in order, off the game thread. It
  tries each event up to three times with the same UUID. Successful requests are
  deduplicated by the running mx_eye process. Restart-persistent deduplication,
  offline replay and connection-loss recording watchdogs are not implemented yet.
- Delivery errors appear in the framework log and its event JSONL. A full
  1024-event queue reports an error instead of blocking the game. Check these
  logs; this initial implementation is not a guarantee of delivery across outages.
- Framework log: `data/eye_events/<run UUID>.jsonl` under the experiment base.
  Each row includes the event, acknowledgement, error and recorder directory.
  The demo's experiment base is `eye_events_demo_data` in the current directory.
- mx_eye saves all received events under `mx_eye_data/events/`. During an owned
  recording it also writes `events.jsonl` and an entry-time `experiment.json`
  beside `video.mkv`, `frames.csv`, `tracking.csv`, `config.json`, `session.json`.
- The same run UUID and visit UUID link both sides. Events also include rig,
  session/trial/stage context, animal and raw RFID where available. RFID updates
  go to events.jsonl; experiment.json remains the entry snapshot. No automatic
  per-animal calibration activation is introduced.
- For two computers, use their normal synchronized system clocks and configure
  the tracker bind/host appropriately. Nothing in this change estimates clock
  offsets. Eye acquisition timestamps exclude camera exposure and USB latency.

The malformed-JPEG stop behavior is unchanged and remains separate work. This
demo validates simulation recording and communications, not Pi camera stability.
