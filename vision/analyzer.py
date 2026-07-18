from ollama import Client

from config import OLLAMA_URL, VISION_MODEL
from vision.prompts import VISION_SYSTEM_PROMPT

class VisionAnalyzer:
    def __init__(self,model:str=VISION_MODEL):
        self.model=model
        self.client=Client(host=OLLAMA_URL)

    def analyze(self,image_path:str,user_prompt:str)->str:
        response=self.client.chat(
            model=self.model,
            messages=[
                {"role": "system",
                    "content": VISION_SYSTEM_PROMPT,},

                {"role": "user",
                    "content": user_prompt,
                    "images": [image_path],},
            ],
        )

        return response['message']['content']