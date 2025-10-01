class Prompt:
    def __init__(self, channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
        base_instructions = [
            "Give your response in a json like format.",
            "It should contain a key 'response' (the script).",
            "Another key 'keywords' should be a list of keywords.",
            "The first element of 'keywords' must be the keyword count.",
            "Ensure keywords are naturally included in the script.",
            "Your response will only contain the json and not any other aspects like markdown or affirmation or thoughts."
        ]
        
        instructions = " ".join(base_instructions)
        
        self.content = {
            "prompt": (
                f"Hey, I want the script for a {video_duration} long video about {video_title}. "
                f"The video is for a channel about {channel_type}. "
                f"{custom_instructions} {instructions}"
            )
        }
