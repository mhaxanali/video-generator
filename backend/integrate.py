from backend.api.genai_api import get_script_and_keywords
from backend.api.images_api.pexels_api import search_images
from backend.api.audio_api.elevenlabs_api import get_tts


def integrate(channel_type, video_title, video_duration, voice_id="JBFqnCBsd6RMkjVDRZzb", custom_instructions=""):
    response = get_script_and_keywords(channel_type, video_title, video_duration, custom_instructions)
    keywords = response['keywords']
    for kw in keywords[1:]:
        search_images(kw, channel_type)
    for each in response["response"]:
        get_tts(each["line"]["text"], voice_id, each["line"]["img_dis"])
