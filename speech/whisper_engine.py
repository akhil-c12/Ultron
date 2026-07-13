from faster_whisper import WhisperModel

class WhisperEngine:
    def __init__(
            self,
            model_size:str="base",
            device:str="cpu",
            compute_type:str="int8",
    ):
        print("loading Whisper")

        