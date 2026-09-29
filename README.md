# AI Video Generator (Modular Pipeline)

> An archived modular AI video generation pipeline designed to orchestrate script creation, image sourcing, text-to-speech, and video clipping.

---

## Project Overview

This project is an **archived full-stack video generation prototype** that was designed to take a video topic and generate video clips through a modular pipeline.

It was built around:

* Backend orchestration of multiple external APIs
* Modular API integration (`GenAI`, `Pexels`, `ElevenLabs`)
* File management and pipeline isolation
* Video editing and clip generation
* Separation of concerns between API integrations and video processing

**Status:** Archived/inactive. The project was not completed into a fully functional end-to-end application. Some components are placeholders, and real-world API constraints and rate limits prevented full deployment.

---

## Architecture

```text
User Input
   ↓
GenAI API (script + keywords)
   ↓
Pexels API (image search)
   ↓
ElevenLabs API (TTS)
   ↓
Video Stitcher (make_clip, combine_clips)
   ↓
Final Video Output
```

The architecture represents the intended pipeline. The repository does not currently provide a complete working implementation of every stage.

## Module Responsibilities

`backend.api.genai_api`: Generates the script and associated keywords for the video
`backend.api.images_api.pexels_api`: Searches for images based on keywords
`backend.api.audio_api.elevenlabs_api`: Generates text-to-speech audio for each line
`backend.video_stitcher`: Combines audio and images into video clips
`backend.integrate`: Intended to orchestrate the full pipeline

## Repo Structure

```text
video-generator/
│   .env                  # Local API keys/configuration; must not be committed
│   .gitignore             # Git ignore rules
│   README.md              # Project documentation
│   requirements.txt       # Python dependencies
│
├── backend/               # Backend pipeline and orchestration
│   │   app.py             # Placeholder/empty backend entry point
│   │   integrate.py       # Pipeline orchestration logic
│   │   video_stitcher.py  # Video clip creation and combination logic
│   │   __init__.py        # Marks backend as a Python package
│   │
│   ├── api/               # API integration modules
│   │   │
│   │   ├── genai_api.py       # Script + keyword generation
│   │   │   __init__.py
│   │   │
│   │   ├── audio_api/         # TTS services
│   │   │       elevenlabs_api.py
│   │   │       __init__.py
│   │
│   │   └── images_api/        # Image sourcing services
│   │           pexels_api.py
│   │           __init__.py
│   │
│   └── assets/                # Supporting constants and prompt classes
│           constants.py
│           prompt.py
│           __init__.py
│
└── frontend/              # Frontend UI for testing/display
        index.html
        script.js           # Placeholder/empty frontend logic file
        style.css
```

## Limitations

* Project is archived and not actively maintained
* The repository does not currently represent a complete working end-to-end application
* `backend/app.py` is empty and does not provide an implemented backend entry point
* `frontend/script.js` is empty and does not provide implemented frontend behavior
* API constraints (rate limits, relevance, cost) limited full execution
* Not all edge cases are handled (e.g., missing images or failed TTS)
* Video stitching is basic — no transitions, timing adjustments, or complex editing
* Intended for short videos (~30–60s) only
* The project depends on external APIs that require valid credentials and may change independently of the repository

## Security Note

The repository previously included a change indicating that `.env` files should be ignored going forward.

If `.env` was committed in an earlier revision, any API credentials present in that historical version should be considered **potentially exposed**, even if the file was later removed or added to `.gitignore`.

Relevant credentials may include:

* GenAI API keys
* Pexels API keys
* ElevenLabs API keys

If historical commits contain real credentials, those credentials should be revoked and replaced. Removing the file from the current working tree does not remove secrets from Git history.

For local development, API credentials should be stored in an untracked `.env` file and should never be committed.

## Future Improvements

If revived, potential upgrades include:

* Implementing the backend API entry point
* Implementing the frontend interaction layer
* Completing the end-to-end generation pipeline
* Support for longer videos with multiple segments
* Retry/fallback logic for failed API requests
* Improved video stitching (transitions, pacing, subtitles)
* Local caching of images/audio to reduce API calls
* Dockerized pipeline for reproducibility
* Integration with asynchronous pipelines for speed
* Secure secret management and credential validation

## Notes

* This project is archived for educational purposes.
* The repository should be considered a prototype rather than a production-ready application.
* The architecture demonstrates an attempt at separating API integrations, orchestration, and media processing.
* Some files are incomplete or empty, including the backend and frontend entry-point files.
* If the project is revived, its Git history should be audited for accidentally committed API credentials before reusing any external services.
* Latest commits merge work from different branches.
