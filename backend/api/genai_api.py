import re
import ast
import google.generativeai as genai
from backend.assets.constants import GEMINI_API_KEY
from backend.assets.prompt import Prompt

genai.configure(api_key=GEMINI_API_KEY)


def get_script_and_keywords(channel_type: str, video_title: str, video_duration: str, custom_instructions: str = ""):
    model = genai.GenerativeModel("gemini-2.5-pro")
    prompt = Prompt(channel_type, video_title, video_duration, custom_instructions)

    response = model.generate_content(prompt.content['prompt'])
    text = response.text.strip()

    # Remove code fences (```python or ```json)
    text = re.sub(r"^```[a-zA-Z]*|```$", "", text).strip()

    # Extract content inside braces if Gemini adds extra text
    if '{' in text and '}' in text:
        text = text[text.index('{') : text.rindex('}') + 1]

    # Basic cleanup for trailing commas or broken brackets
    cleaned = (
        text.replace(",]", "]")
        .replace(",}", "}")
        .replace("True", "True")   # keep as Python literal
        .replace("False", "False")
        .replace("None", "None")
    )

    # Try parsing safely
    try:
        return ast.literal_eval(cleaned)
    except SyntaxError:
        # Attempt auto-fix for unclosed brackets
        if cleaned.count('[') > cleaned.count(']'):
            cleaned += ']'
        if cleaned.count('{') > cleaned.count('}'):
            cleaned += '}'
        try:
            return ast.literal_eval(cleaned)
        except Exception as e:
            print("\n--- Gemini output caused syntax error ---")
            print(cleaned)
            raise e
