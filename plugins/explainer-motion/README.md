# explainer-motion

Make vertical "faceless" explainer and app-promo videos for TikTok, Reels and Shorts: a
mascot sticker that changes pose on every phrase, captions that light up word by word, and
UI cards synced to a voice-over. Rendered from HTML with HyperFrames — no video-generation
model.

## Skills

| Skill | What it does |
| --- | --- |
| `explainer-video-pipeline` | Runs the whole pipeline: prerequisites, project layout, build, render, review. Start here. |
| `explainer-script-and-beats` | Writes the 20–45 s script and the beats that place poses, cards and titles on phrases. |
| `explainer-mascot-poses` | Creates or adopts the mascot, generates its pose bank and cuts each pose out as a sticker. |
| `explainer-voiceover` | Produces the voice-over and word timings: your recording, a local VoiceStudio clone, ElevenLabs, or a placeholder. |

## Requirements

`bun`, `ffmpeg`, `node`/`npx`, `python3`, and the HyperFrames CLI (`npx hyperframes doctor`).
Optional: a Vercel AI Gateway key for character images, an ElevenLabs key for voices.

Ask your agent: "Make an explainer video for my app" — it starts with the pipeline skill.
