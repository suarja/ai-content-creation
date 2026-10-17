"""Generate a VoiceStudio voice-over one script line at a time, then assemble it.

A clone asked for the whole script at once rushes some sentence ends and drags others.
One request per line gives each line its own natural ending; the lines are then trimmed
and joined with even pauses: --pause after a line ending in . ? ! …, --short otherwise.

Usage: python3 -I voice_by_line.py <project> --ref-start S --ref-end E [--speed 1.1]
       [--seed 42] [--pause 0.30] [--short 0.18] [--only 3,7] [--url http://127.0.0.1:3900]
Needs voice/reference.wav and voice/reference/transcript.json from a previous
`voice.py voicestudio` run with the same window. Writes voice/lines/*.wav and
voice/narration.wav; then run `voice.py transcribe <project>`.
"""

import argparse
import json
import re
import subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("--speed", type=float, default=1.1)
ap.add_argument("--seed", type=int, default=42)
ap.add_argument("--pause", type=float, default=0.30)
ap.add_argument("--short", type=float, default=0.18)
ap.add_argument("--ref-start", type=float, required=True)
ap.add_argument("--ref-end", type=float, required=True)
ap.add_argument("--url", default="http://127.0.0.1:3900")
ap.add_argument("--only", help="comma-separated line numbers to regenerate (1-based); others are reused")
a = ap.parse_args()

P = Path(a.project)
V = P / "voice"
L = V / "lines"
L.mkdir(parents=True, exist_ok=True)
cfg = json.loads((P / "project.json").read_text())
lang = {"fr": "French", "en": "English", "es": "Spanish", "de": "German", "pt": "Portuguese"}.get(cfg.get("lang"), "Auto")
pron = (cfg.get("voice") or {}).get("pronounce") or {}

ref = V / "reference.wav"
rw = json.loads((V / "reference/transcript.json").read_text())
rw = rw if isinstance(rw, list) else rw["words"]
ref_text = " ".join(w["text"] for w in rw if w["start"] >= a.ref_start - 0.05 and w["end"] <= a.ref_end + 0.05)

lines = [l.strip() for l in (P / "script.txt").read_text().splitlines() if l.strip() and not l.startswith("#")]
only = {int(x) for x in a.only.split(",")} if a.only else None


def run(*cmd: str) -> None:
    subprocess.run(cmd, check=True)


parts = []
for n, line in enumerate(lines, 1):
    clean = L / f"{n:02d}.wav"
    if only is None or n in only or not clean.exists():
        text = line
        for k, v in pron.items():
            text = re.sub(rf"\b{re.escape(k)}\b", v, text)
        gen = L / f"{n:02d}.gen.wav"
        run("curl", "-sf", "-m", "600", "-X", "POST", a.url.rstrip("/") + "/generate",
            "-F", f"text={text}", "-F", f"ref_audio=@{ref}", "-F", f"ref_text={ref_text}",
            "-F", f"language={lang}", "-F", f"seed={a.seed}", "-F", f"speed={a.speed}", "-o", str(gen))
        # Trim the silence the engine leaves before and after the line. A harder threshold
        # eats soft first syllables.
        run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(gen), "-ac", "1", "-ar", "44100", "-af",
            "silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.08,"
            "areverse,silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.10,areverse,"
            "afade=t=in:d=0.01", str(clean))
        print(f"✓ line {n:02d}: {line}")
    end = line.rstrip()[-1]
    gap = a.pause if end in ".?!…" else a.short
    parts.append((clean, gap if n < len(lines) else 0.4))

# Assemble: each line, then its pause; loudness evened over the whole.
concat = V / "lines.txt"
with concat.open("w") as f:
    for wav, gap in parts:
        sil = L / f"sil-{int(gap * 1000)}.wav"
        if not sil.exists():
            run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                "anullsrc=r=44100:cl=mono", "-t", str(gap), str(sil))
        f.write(f"file '{wav.resolve()}'\nfile '{sil.resolve()}'\n")
run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
    "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", str(V / "narration.wav"))
print(f"✓ voice/narration.wav from {len(parts)} lines")
