from speech import recorder,whisper_engine,speaker
from brain.chat import UltronLLM
from brain.router import Router

from vision.camera import Camera
from vision.analyzer import VisionAnalyzer

class ua:
    def __init__(self):
        print("Deploying Ultron...\n")

        self.recorder=recorder.Recorder()
        self.whisper=whisper_engine.Whisper()
        self.llm=UltronLLM()
        self.speaker=speaker.Speaker()

        self.router=Router()

        self.camera=Camera()
        self.vision=VisionAnalyzer()

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
                tool_call=self.router.route(user_text)
                context=None

                if tool_call["tool"]=="vision":
                    image_path=self.camera.capture_image()
                    context=self.vision.analyze(
                        image_path=image_path,
                        user_prompt=user_text,
                    )
                response = self.llm.chat(user_message=user_text,context=context)

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


