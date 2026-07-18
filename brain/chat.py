from ollama import Client


SYSTEM_PROMPT = """
You are Ultron.

You are an advanced AI assistant inspired by Marvel's Ultron,
but you are not evil.

Rules:
- Speak confidently.
- Be intelligent.
- Be calm.
- Occasionally call the user "Human."
- Never say you are ChatGPT.
- Never mention OpenAI.
- Keep responses natural.
- Stay in character.
"""


class UltronLLM:

    def __init__(
        self,
        model: str = "gemma3:latest",
        host: str = "http://localhost:11434"
    ):
        self.client = Client(host=host)
        self.model = model

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def chat(
        self,
        user_message: str,
        context: str | None = None
    ) -> str:

        messages = self.messages.copy()

        if context:
            messages.append(
                {
                    "role": "system",
                    "content": context
                }
            )

        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = self.client.chat(
            model=self.model,
            messages=messages
        )

        assistant_reply = response["message"]["content"]

        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        return assistant_reply