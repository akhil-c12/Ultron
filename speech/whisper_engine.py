from faster_whisper import WhisperModel

class Whisper:
    def __init__(
            self,
            model_size:str="base",
            device:str="cpu",
            compute_type:str="int8",
    ):
        print("loading Whisper")

        self.model=WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

        print("whisper Ready")

    def transcribe(self,audio_path:str)->str:

        segments,info=self.model.transcribe(audio_path)
        text=""

        for segment in segments:
            text+=segment.text

        text=text.strip()

        print(f"\nYou:{text}")

        return text