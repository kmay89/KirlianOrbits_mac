"""Regression tests for the pure-Python sequencer engine.

These intentionally exercise only ``sequencer.py``, which depends solely on the
standard library — so they run in CI without needing pygame or python-rtmidi.
"""

import math

import sequencer
from sequencer import (
    Sequencer,
    midi_to_name,
    name_to_midi,
    get_notes_in_scale,
)


def test_midi_name_roundtrip():
    for m in (24, 36, 48, 60, 61, 67, 72, 84):
        assert name_to_midi(midi_to_name(m)) == m


def test_midi_to_name_examples():
    assert midi_to_name(60) == "C4"
    assert midi_to_name(69) == "A4"
    assert midi_to_name(61) == "C#4"


def test_get_notes_in_scale_c_major():
    assert get_notes_in_scale(0, "Major", 60, 72) == [60, 62, 64, 65, 67, 69, 71, 72]


def test_get_notes_in_scale_unknown_falls_back_to_chromatic():
    assert get_notes_in_scale(0, "NotARealScale", 60, 63) == [60, 61, 62, 63]


def test_sequencer_defaults():
    seq = Sequencer()
    assert seq.bpm == 120
    assert seq.is_playing is False
    assert len(seq.notes) == 3


def test_add_and_remove_note():
    seq = Sequencer()
    n = seq.add_note(50.0, 0.0)
    assert n in seq.notes
    seq.remove_note(n)
    assert n not in seq.notes


def test_note_polar_cartesian_consistency():
    seq = Sequencer()
    n = seq.notes[0]
    n.sync_cartesian(seq.clock_radius)
    assert abs(math.hypot(n.x, n.y) - n.norm_r * seq.clock_radius) < 1e-6


class _FakeMidi:
    """Minimal stand-in capturing the notes the sequencer asks to play."""

    def __init__(self):
        self.sent = []

    def send_note_on(self, midi_note, velocity, channel, gate_length_sec):
        self.sent.append((midi_note, velocity, channel))


def test_spinning_arm_triggers_notes(monkeypatch):
    # Drive time deterministically so the sweep advances regardless of wall clock.
    clock = {"t": 1000.0}
    monkeypatch.setattr(sequencer.time, "time", lambda: clock["t"])

    seq = Sequencer()
    seq.is_line_spinning = True
    seq.start()

    midi = _FakeMidi()
    for _ in range(600):
        clock["t"] += 1.0 / 60.0
        seq.update(midi)

    assert len(midi.sent) > 0


def test_save_load_roundtrip(tmp_path):
    seq = Sequencer()
    seq.set_bpm(143)
    path = tmp_path / "session.json"
    seq.save_to_json(str(path))

    loaded = Sequencer()
    loaded.load_from_json(str(path))
    assert loaded.bpm == 143
    assert len(loaded.notes) == len(seq.notes)
