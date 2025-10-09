from backend.api.genai_api import get_script_and_keywords
from backend.api.images_api.pexels_api import search_images
from backend.api.audio_api.elevenlabs_api import get_tts


def download_relevant_images(channel_type, video_title, video_duration, custom_instructions=""):
    response = get_script_and_keywords(channel_type, video_title, video_duration, custom_instructions)
    keywords = response['keywords']
    for i, kw in enumerate(keywords):
        if i == 0:
            pass
        else:
            search_images(kw, channel_type)


def get_tts_audio(text, voice_id="JBFqnCBsd6RMkjVDRZzb"):
    get_tts(text, voice_id)


