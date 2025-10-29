# Autoreel Generator App Documentation

## Utilization
WebApp will take multiple inputs from a form and generate a video ready to be uploaded on YouTube Shorts, TikTok, Instagram Reels and other platforms. Following steps will be taken:

1. From GenAI API (Currently using Gemini API), the backend will recieve a script and keywords.
2. Relevant Images will be found using `backend/api/images_api/` and placed inside `downloads/images`.
3. TTS will be generated of each line separately using `backend/api/audio_api/` and placed inside `downloads/audio`.
4. Video will be stitched together using `backend/video_stitcher.py`.

## Notes
- Always run python files as modules from project root:
    ```bash
    python -m backend.integrate
    ```