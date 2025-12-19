from backend.api.genai_api import get_script_and_keywords
from backend.api.images_api.pexels_api import search_images
from backend.api.audio_api.elevenlabs_api import get_tts
from backend.video_stitcher import make_clip, combine_clips
from shutil import rmtree
import os


def integrate(channel_type, video_title, video_duration, voice_id="JBFqnCBsd6RMkjVDRZzb", custom_instructions=""):
    response = get_script_and_keywords(channel_type, video_title, video_duration, custom_instructions)
    keywords = response['keywords']
    hlp = []

    if os.path.exists("downloads"):
        rmtree("downloads", ignore_errors=True)

    for kw in keywords[1:]:
        search_images(kw, channel_type)

    for each in response["response"]:
        get_tts(each["line"]["text"], voice_id, each["line"]["img_dis"])
        os.makedirs(os.path.join('downloads', 'output'), exist_ok=True)
        make_clip(each["line"]["text"], os.path.join('downloads', 'images', f'{each['line']['img_dis']}_1.jpg'), os.path.join('downloads', 'audio', f'{each['line']['img_dis']}.mp3'), os.path.join('downloads', 'output', f'{each['line']['img_dis']}.mp4'))
        hlp.append(f'{each['line']['img_dis']}')


if __name__ == '__main__':
    integrate('facts', 'that one time napolean was attacked by rabbits', '30s')