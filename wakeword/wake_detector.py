import numpy as np
import sounddevice as sd
from openwakeword.model import Model

class WakeWordDetector:
    def __init__(self):
        self.sample_rate=16000
        self.chunk_size=1280
        self.threshold=0.5

        self.model=Model()

    def listen(self):
        print("Listening")

        with sd.InputStream(
        samplerate=self.sample_rate,
        channels=1,
        dtype="int16",
        blocksize=self.chunk_size,        
        ) as stream:
            while True:
                audio,overflow=stream.read(self.chunk_size)

                audio=np.squeeze(audio)

                for wakeword,score in predictions.items():
                    if score>self.threshold:
                        print(f"\n✅ Wake Word Detected: {wakeword}")
                        print(f"Confidence: {score:.2f}")
                        return wakeword
    