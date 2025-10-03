from backend.api.genai_api import get_script_and_keywords
from backend.api.images_api.unsplash_api import search_images
from backend.assets.constants import EXAMPLE_VIDEO_DETAILS


def download_relevant_images(channel_type, video_title, video_duration, custom_instructions=""):
    response = get_script_and_keywords(channel_type, video_title, video_duration)
    keywords = response['keywords']
    for i, kw in enumerate(keywords):
        if i == 0:
            pass
        else:
            search_images(kw)


if __name__ == '__main__':
    v = EXAMPLE_VIDEO_DETAILS
    download_relevant_images(v['channel_type'], v['video_title'],v['video_duration'])