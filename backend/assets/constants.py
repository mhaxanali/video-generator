import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
UNSPLASH_ACCESS_KEY=os.getenv("UNSPLASH_ACCESS_KEY")

EXAMPLE_VIDEO_DETAILS = {
    "channel_type": "facts",
    "video_title": "that one time napolean was attacked by rabbits",
    "video_duration": ""
}
