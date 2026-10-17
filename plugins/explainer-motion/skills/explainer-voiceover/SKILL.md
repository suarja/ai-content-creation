---
name: explainer-voiceover
description: Produce the voice-over of a mascot explainer video and its word-level timings — from the user's own recording, a free local voice clone in VoiceStudio, ElevenLabs, or a macOS placeholder — then check it says the script. Use when an explainer-video-pipeline project needs its narration, when the user wants to clone their voice, change provider, fix a mispronounced name, or speed the delivery up, when a cloned voice rushes or drags between sentences (generate it line by line), when the voice must match the author's real pauses, or when the clone sounds worse than the author and must be improved.
---

# Voice-over

Every provider writes `voice/narration.wav`, then the same step transcribes it word by
word (voice/transcript.json) and compares it with script.txt. The video build only
reads those two files, so changing provider never touches the beats.

```bash
python3 -I <skill>/scripts/voice.py <provider> <project> [options]
```

## Choose with the user

| Provider | Cost | Quality / effort | Use when |
| --- | --- | --- | --- |
| `recording` | free | best, their real voice; needs a quiet room and one clean read | they are fine speaking; the format's author uses their own voice |
| `voicestudio` | free, local | a clone of their voice from ~15 s of reference; 2–4 min per generation on Apple Silicon | they want their voice without re-recording each script |
| `elevenlabs` | paid API | studio clone or stock voice, fast | they already have an ElevenLabs voice or want a stock voice |
| `say` | free | robotic | placeholder to build and time the video before the real voice exists. Never publish |

Clone only a voice the user owns or has permission to use.

## recording

Ask for one read of script.txt in a quiet room, phone or USB mic 15–20 cm away, a
bit faster and more energetic than conversation. Then:

```bash
python3 -I voice.py recording <project> --file take.m4a
```

Silences are shortened to 0.25 s and loudness normalised. Mistakes and retakes stay:
read the fidelity report, cut them by hand (`ffmpeg -ss/-to` and concat) or re-read
the line, then `voice.py transcribe <project>`.

## voicestudio (local clone)

Setup, once (the user's machine, with their consent for each download):

1. Download `VoiceStudio-Electron-<version>-mac-arm64.dmg` from
   github.com/debpalash/VoiceStudio/releases (≈ 250 MB), compare its SHA-256 with the
   release's SHA256SUMS.txt, copy `VoiceStudio.app` to `/Applications`. It is not
   notarised: first launch is right-click → Open. Leave the analytics prompt to them.
2. In the app, accept the clone model install (OmniVoice, ≈ 2.4 GB; ≈ 10 GB in all
   with its Python runtime). Intel Macs cannot run the backend.
3. The user records a profile in **Voice cloning**: 30–60 s of natural speech, ideally
   in the tone of the videos. They tell you its name.

Generate:

```bash
python3 -I voice.py voicestudio <project> --profile "My voice" [--speed 1.1]
```

The backend listens on `http://127.0.0.1:3900`. The engine keeps at most ~20 s of
reference and needs the exact transcript of that window (or an STT model selected in
the app, otherwise `/generate` fails with "Automatic reference transcription needs an
installed speech-to-text model"). The script handles it: it downloads the profile's
audio, transcribes it, cuts a window of whole sentences (8–18 s) into
`voice/reference.wav`, and sends it with its text.

**The window changes the result.** Measured on one profile: an automatic 15 s window
gave 145 words/min and 16 % divergence from the script (words changed); a hand-picked
13 s sentence spoken fluently gave 188 words/min and 4 %. The script prints the
candidate windows; when the report is above ~10 % or the pace drags, retry with
another one:

```bash
python3 -I voice.py voicestudio <project> --profile "My voice" --ref-start 34.5 --ref-end 47.4
```

Pick a sentence said in one breath, with no restart or hesitation.

### Line by line (natural prosody)

A clone asked for the whole script in one request chains some sentences without a
breath and drags others. The owner heard it at once: the words tumble into each other.
Generate one request per script line instead, trim each line's silence, and join them
with even pauses:

```bash
python3 -I voice.py voicestudio <project> --profile "My voice" --ref-start 34.5 --ref-end 47.4   # once: writes the reference
python3 -I <skill>/scripts/voice_by_line.py <project> --ref-start 34.5 --ref-end 47.4 --speed 1.12 --pause 0.24 --short 0.14
python3 -I voice.py transcribe <project>
```

- **A script line is a breath group** (2–6 words, see `explainer-script-and-beats`).
  `--pause` follows a line ending in `. ? ! …`, `--short` any other line.
- **The pause you hear is longer than the one you set**: each trimmed line keeps about
  0.08 s of silence before and 0.10 s after. Measured on 11 Oct 2026: set 0.14/0.24,
  heard a 0.43 s median; the author speaks with 0.16 s pauses. Set the pauses lower
  rather than tightening the trim, which eats soft first syllables. Second episode,
  `--speed 1.2 --pause 0.18 --short 0.10`: 164 words/min, 57 pauses/min, 0.33 s median —
  closer, still slower than the author.
- **The clone sometimes swallows the start of a very short line** ("He says that"
  vanished twice, with two seeds; "he reads it again" too). Merge that line with the
  previous one and regenerate only it: `--only <n>` reuses every other line, so a fix
  costs one request. After a merge, the line numbers shift: rename the cached line files
  (voice/lines/NN) to their new numbers before regenerating, or every later line is
  regenerated.
- **The clone can also add a word** (an extra *of* in "it's not even me talking"): a new
  `--seed` on that line with `--only` fixed it.
- **Check each line, not only the total**: the report's 15–23 % difference with the
  script hides which line failed. Transcribe a suspect line's file alone with
  `npx hyperframes transcribe` (model small, the script's language) and read what the
  clone said. "pose" read back as "pause" is a homophone, not an error.
- Cost: about 20 s per line, 8–15 min for a 45 s video, against 3 min in one request.
- Never re-time a single-request voice by cutting inside sentences: a first tool did,
  the owner heard it as jerky. Only whole lines move.

### When the clone is not good enough

One French episode (51.9 s, line by line, speed 1.2): the owner judged that the cloned
voice hurt the video, and that English terms sounded wrong ("reverse engineering" first
came out "reverse energy marine"; "ElevenLabs" respelled phonetically for French sounded
odd). What the research says (Oct 2026, mostly vendor guides, no French benchmark), and
what to try, cheapest first:

1. **The author records the line themselves.** Best quality, two minutes of work, and the
   format's own author uses their voice. Mix it: their recording for the hook and the
   foreign terms, the clone elsewhere, or their recording for the whole script
   (`recording` provider).
2. **A better reference.** Quality depends on the reference clip more than its length: one
   speaker, no noise or reverb, no leading silence, mono WAV, exact transcript, 10 to 30 s in
   the energy of the videos (not a calm read). Record a dedicated 30–60 s profile in that tone
   and test three windows (10, 15, 30 s) on the same two lines before regenerating a script.
3. **Keep foreign terms out of the clone.** Write the native form when it exists, or record
   the term, or test two respellings on that one line with `--only` and transcribe it. Never
   ship a respelling nobody has listened to.
4. **Another local model, blind-tested.** Chatterbox Multilingual (MIT, multilingual, runs on
   Apple MPS, clones from ~10 s) and Qwen3-TTS (many languages, slow on a Mac) are the
   candidates. Run the same two lines with the same reference through each, let the owner
   pick blind.
5. **Paid**: ElevenLabs Professional Voice Clone (30+ min of audio) is the studio-grade option.

Licence check: OmniVoice, the model behind VoiceStudio, ships weights under CC BY-NC
(non-commercial). Videos that promote a paid product are commercial use: say so to the owner
before publishing with it.

### Match the author's timing

Measure the author's real pauses from their published videos, then compare the
generated voice:

```bash
yt-dlp -x --audio-format m4a -o "%(upload_date)s-%(id)s.%(ext)s" --write-info-json "https://www.tiktok.com/@<handle>"
python3 -I <skill>/scripts/speech_timing.py <audio dir> --compare <project>/voice/narration.wav
```

Ask before downloading (filename, source, size) and keep the audio out of git.
Speech-to-text word timings cannot measure pauses — Whisper stretches each word over the
gap after it — so the script uses silence detection on the audio. Videos with music
under the voice show almost no pause and are reported apart. On one creator's account
(73 videos): about 110 short pauses a minute, 0.16 s median, 180 words a minute.

## elevenlabs

```bash
export ELEVENLABS_API_KEY=...
python3 -I voice.py elevenlabs <project> --voice-id <id> [--model eleven_multilingual_v2] [--speed 1.1]
```

The voice id is in the ElevenLabs voice library (their cloned voice or a stock one).
`eleven_multilingual_v2` handles French and most languages.

## say (placeholder)

```bash
python3 -I voice.py say <project> --voice Samantha    # `say -v '?'` lists voices per language
```

Use it to build and review the video while the real voice is pending.

## Pronunciation and pace

- A name said wrong by a synthetic voice: add a respelling in project.json,
  `"voice": { "pronounce": { "Recap": "Ree-cap" } }`. It changes only the text sent to the
  voice; captions keep the script's spelling.
- A foreign term is read in the voice's own language (an English term in a French voice
  sounds French): respell it, then listen. Results with a French voice: "reverse
  engineering" respelled "rivers ènedjinirine" gave "reverse energy marine"; "riveurse
  ènedjiniringue" passed the transcription but still sounded odd to the owner;
  "ElevenLabs" → "Éleveune Labs" sounded wrong. For an identifier, respell it word by word
  ("subagentPromptCacheTtl" → "seube agent, prompte cache, T T L"). It stays
  approximate; put the exact spelling on a card at that moment.
- Pace: the reference videos run 190–245 words/min. The report prints the rate; use
  `--speed 1.1`–`1.2` (VoiceStudio, ElevenLabs) when it drags.

## The report

```
✓ voice/transcript.json · 98 words · 30.4s · 193 words/min
  difference with script.txt: 4%
  pauses over 0.6s: [...]
```

Names and numbers spelled differently by speech-to-text are normal (the build aligns
them back to the script). Above ~15 %, listen: words were skipped, changed or invented.
Then let the user listen before rendering the final: whether a clone sounds like them
is their call, not the report's.
