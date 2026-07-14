from speech import recorder,whisper_engine,speaker
from llm import UltronLLm


class ua:
    def __init__(self):
        print("Deploying Ultron...\n")

        self.recorder=recorder.Recorder()
        self.whisper=whisper_engine.Whisper()
        self.llm=UltronLLm()
        self.speaker=speaker.Speaker()

    def run(self):
        self.speaker.speak("Greetings, Human. Ultron is now online.")

        while True:
            try:
                audio_path = self.recorder.record()

                user_text = self.whisper.transcribe(audio_path)

                if not user_text.strip():
                    continue

                print(f"\nHuman : {user_text}")

                if user_text.lower() in [
                    "exit",
                    "quit",
                    "shutdown ultron",
                    "goodbye"
                ]:
                    self.speaker.speak("Shutting down. Until next time, Human.")
                    break

                response = self.llm.chat(user_text)

                print(f"\nUltron : {response}")

                self.speaker.speak(response)

            except KeyboardInterrupt:

                self.speaker.speak("Emergency shutdown initiated.")
                break

            except Exception as e:

                print(f"\nError: {e}")
                self.speaker.speak(
                    "An unexpected error occurred."
                )


