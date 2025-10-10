class Prompt:
    def __init__(self, channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
        response_structure = """
        {
            "response": [
                {"line": {"type": "hook", "text": "string", "img_dis": "keyword1"}},
                {"line": {"type": "payload", "text": "string", "img_dis": "keyword2"}},
                {"line": {"type": "ending", "text": "string", "img_dis": "keywordN"}}
            ],
            "keywords": [N, "keyword1", "keyword2", "keywordN"]
        }
        """

        base_instructions = [
            "Give your response in a json like format.",
            "It should contain a key 'response' (the script).",
            "Another key 'keywords' should be a list of keywords. The keywords should be relevant as they would be used to find images using API to make the video.",
            "The first element of 'keywords' must be the keyword count.",
            "Ensure keywords are naturally included in the script.",
            "Your response will only contain the json and not any other aspects like markdown or affirmation or thoughts.",
            f"response should not contain any timestamps or anything and should be like {response_structure}",
            "Keywords should be image search friendly for pexels api.",
            "Script should be complete with a hook at the start to improve user retention and end with a sentence to improve user engagement."
        ]
        
        instructions = " ".join(base_instructions)
        
        self.content = {
            "prompt": (
                f"Hey, I want the script for a {video_duration} long video about {video_title}. "
                f"The video is for a channel about {channel_type}. "
                f"{custom_instructions} {instructions}"
            )
        }
