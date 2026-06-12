import edge_tts
import asyncio
import pygame
import io

class Speaker:
    def __init__(self, voice="en-US-AriaNeural"):
        self.voice = voice
        pygame.mixer.init()

    def say(self, text: str):
        asyncio.run(self._speak(text))

    async def _speak(self, text: str):
        communicate = edge_tts.Communicate(text, self.voice)
        audio_stream = io.BytesIO()

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_stream.write(chunk["data"])

        audio_stream.seek(0)
        pygame.mixer.music.load(audio_stream)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(10)