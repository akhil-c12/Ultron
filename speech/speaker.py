import asyncio
import edge_tts
import pygame
from pathlib import Path

class Speaker:

    def __init__(self):
        self.voice="en-US-GuyNeural"

        self .output_dir=Path("assets/audio")
        self.output_dir.mkdir(parents=True,exist_ok=True)

        pygame.mixer.init()

    async def _generate(self,text:str,output:str):
        communicate=edge_tts.Communicate(text=text,voice=self.voice)
        await communicate.save(output)

    def speak(self,text:str):
        output=self.output_dir/"response.mp3"
        asyncio.run(self._generate(text,output))
        pygame.mixer.music.load(str(output))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

















        