from backend.assets.constants import ELEVENLABS_API_KEY
from elevenlabs import ElevenLabs

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def get_tts(text: str, voice_id: str):
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_turbo_v2",
        text=text,
        output_format="mp3_44100_128"
    )

    audio_bytes = b"".join(audio)
    save_audio(audio_bytes)


def save_audio(audio_bytes):
    with open("output.mp3", "wb") as f:
        f.write(audio_bytes)
