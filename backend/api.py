import requests
import google.generativeai as genai
import ast
from constants import GEMINI_API_KEY
from prompt import Prompt

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def get_script_and_keywords(channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
    prompt = Prompt(channel_type, video_title, video_duration, custom_instructions)

    response = model.generate_content(prompt.content['prompt'])
    cleaned = response.text.replace('```', '') if response.text.startswith('```') and response.text.endswith('```') else response.text
    if cleaned[0] != '{':
        cleaned = '{' + cleaned.split('{')[1]
    return ast.literal_eval(cleaned)


def get_images():
    ...
