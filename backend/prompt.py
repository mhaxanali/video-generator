class Prompt:
    def __init__(self, channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
        base_instructions = [
            "Give your response in a json like format.",
            "It should contain a key 'response' (the script).",
            "Another key 'keywords' should be a list of keywords. The keywords should be relevant as they would be used to find images using API to make the video.",
            "The first element of 'keywords' must be the keyword count.",
            "Ensure keywords are naturally included in the script.",
            "Your response will only contain the json and not any other aspects like markdown or affirmation or thoughts.",
            "response should not contain any timestamps or anything and should be like {'response': ' The script with a hook at the start and a line at the end to improve viewer retention. ', 'keywords': [n, 1st keyword, 2nd keyword, nth keyword]} where the number of keywords are 1 for every 3-5 seconds of video."
        ]
        
        instructions = " ".join(base_instructions)
        
        self.content = {
            "prompt": (
                f"Hey, I want the script for a {video_duration} long video about {video_title}. "
                f"The video is for a channel about {channel_type}. "
                f"{custom_instructions} {instructions}"
            )
        }
