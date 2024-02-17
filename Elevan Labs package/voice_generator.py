from elevenlabs import Voice, VoiceSettings, voices, generate, play
import os
from dotenv import load_dotenv

voice_list = voices()
audio = generate(
    text="Like and subscribe.",
    voice=Voice(
        voice_id="LcfcDJNUP1GQjkzn1xUU",
        settings=VoiceSettings(stability=0.7, similarity_boost=0.5)
    ),
    model="eleven_monolingual_v1"
)

print(voice_list)
play(audio)