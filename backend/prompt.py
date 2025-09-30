
class Prompt:
    def __init__(self, channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
        instructions: str = "Give your response in a python dict like format. It should contain a key 'response' and another key 'keywords' which will be a python list of keywords (you will give the amunt of keywords as the first element of the list). These keywords will be used to find stock images that will be used to make the video. Make sure that the keywords are also used in the script."
        self.content: dict = {
            "prompt": f"Hey, I want the script for a {video_duration} long video about {video_title}, the video is for a channel about {channel_type}.{custom_instructions + " " + instructions}"
        }
