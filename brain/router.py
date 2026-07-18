import json
from ollama import Client

from config import OLLAMA_URL

ROUTER_PROMPT="""
You are Ultron's routing engine.

Your ONLY responsibility is deciding whether the user's request requires a tool.

Available tools:

1. vision
Description:
Use when the user asks about something visible through the webcam.
Examples:
- What am I holding?
- What do you see?
- Describe my surroundings.
- Is this cable damaged?

If no tool is needed, return "none".

Return ONLY valid JSON.

Examples:

{
    "tool": "vision",
    "arguments": {}
}

{
    "tool": "none",
    "arguments": {}
}

Do NOT answer the user's question.
Do NOT explain your reasoning.
Return JSON only.
"""


class Router:
    def __init__(self,model:str="gemma3:latest"):
        self.client=Client(host=OLLAMA_URL)
        self.model=model

    def route(self,user_message:str)->dict:

        response=self.client.chat(
            model=self.model,
            messages=[
                {
                    "role":"system",
                    "content":ROUTER_PROMPT,
                },
                {
                    "role":"user",
                    "content":user_message,
                },
            ],
        )

        content=response["message"]["content"]
        
        try:
            return json.loads(content)

        except json.JSONDecodeError:
            pass

        return {
            "tool":"name",
            "arguments":{},
        }