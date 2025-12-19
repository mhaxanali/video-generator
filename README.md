# AI Video Generator (Modular Pipeline)

> A modular AI-powered video generation pipeline that orchestrates script creation, image sourcing, text-to-speech, and video clipping.

---

## Project Overview

This project is a **full-stack modular video generator** that takes a video topic and automatically produces video clips using AI APIs.  

It demonstrates:

- Backend orchestration of multiple AI services  
- Modular API integration (`GenAI`, `Pexels`, `ElevenLabs`)  
- File management and pipeline isolation  
- Video editing and clip generation  
- Full-stack design thinking with separation of concerns  

**Status:** Inactive/archived. Real-world API constraints and rate limits prevented full deployment.

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
## Module Responsibilities
`backend.api.genai_api`: Generates the script and associated keywords for the video\
`backend.api.images_api.pexels_api`: Searches for images based on keywords\
`backend.api.audio_api.elevenlabs_api`: Generates text-to-speech audio for each line\
`backend.video_stitcher`: Combines audio and images into video clips\
`backend.integrate`: Orchestrates the full pipeline
## Repo Structure
```
video-generator/
│   .env                  # Private API keys and configuration (ignored in Git)
│   .gitignore             # Git ignore rules
│   README.md              # Project documentation
│   requirements.txt       # Python dependencies
│
├── backend/               # Backend pipeline and orchestration
│   │   app.py             # Entry point for backend API or testing
│   │   integrate.py       # Main orchestration function for pipeline
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
│   │   │
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
        script.js
        style.css
```
## Limitations

- Project is archived and not actively maintained
- API constraints (rate limits, relevance, cost) limited full execution
- Not all edge cases are handled (e.g., missing images or failed TTS)
- Video stitching is basic — no transitions, timing adjustments, or complex editing
- Currently supports short videos (~30-60s) only

## Future Improvements

If revived, potential upgrades include:

- Support for longer videos with multiple segments
- Retry/fallback logic for failed API requests
- Improved video stitching (transitions, pacing, subtitles)
- Local caching of images/audio to reduce API calls
- Dockerized pipeline for reproducibility
- Integration with asynchronous pipelines for speed

## Skills Demonstrated

- Backend orchestration: Managing multiple API services and pipeline flow
- Frontend / full-stack thinking: Preparing outputs consumable by video editors or UIs
- Databases & caching: (planned for future improvement)
- DevOps awareness: Folder isolation, media management, pipeline reproducibility
- Software architecture: Modular, maintainable design with clear separation of concerns
## Notes
- This project is archived for educational purposes.
- Even though the pipeline is incomplete, it serves as a strong example of modular design, orchestration, and full-stack thinking.
- Latest commits merge work from different branches.
