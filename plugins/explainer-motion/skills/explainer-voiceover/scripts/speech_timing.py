"""Measure how someone pauses when they speak, from audio, and compare a generated voice.

Word timings from speech-to-text are useless here: Whisper stretches each word over the
pause that follows it, so every gap reads as zero. Silence detection on the audio works.

Usage: python3 -I speech_timing.py <dir of the author's audio files> [--compare a.wav b.wav ...]
       [--noise -32] [--min 0.08] [--max 1.5]
Prints, as medians over the author's videos: pauses per minute, median pause length and
share of silence; then the same for each --compare file (e.g. voice/narration.wav).
"""

import argparse
import re
import statistics as st
import subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("dir")
ap.add_argument("--compare", nargs="*", default=[])
ap.add_argument("--noise", type=float, default=-32.0, help="silence threshold, dBFS")
ap.add_argument("--min", type=float, default=0.08, help="shortest pause counted, seconds")
ap.add_argument("--max", type=float, default=1.5, help="longer silences are cuts or music, ignored")
a = ap.parse_args()


def measure(path: Path):
    err = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path), "-af", f"silencedetect=noise={a.noise}dB:d={a.min}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err).groups()
    total = int(h) * 3600 + int(m) * 60 + float(s)
    pauses = [float(x) for x in re.findall(r"silence_duration: ([\d.]+)", err) if float(x) <= a.max]
    if total < 10:
        return None
    return {"per_min": len(pauses) / total * 60, "median": st.median(pauses) if pauses else 0.0,
            "share": sum(pauses) / total}


def show(label, rows):
    med = lambda k: st.median(r[k] for r in rows)
    print(f"{label:<30} {med('per_min'):5.1f} pauses/min · median pause {med('median'):.2f}s · silence {med('share'):.0%}")


files = [p for p in sorted(Path(a.dir).iterdir()) if p.suffix.lower() in {".m4a", ".mp3", ".wav", ".mp4", ".aac"}]
rows = [m for p in files if (m := measure(p))]
quiet = sum(1 for r in rows if r["per_min"] < 3)
print(f"{len(rows)} files · {quiet} with almost no pause (music under the voice?)")
show("author (medians)", [r for r in rows if r["per_min"] >= 3] or rows)
for c in a.compare:
    m = measure(Path(c))
    if m:
        show(Path(c).name, [m])
