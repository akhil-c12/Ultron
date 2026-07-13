import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

class Recorder:

    def __init__(
            self,
            sample_rate:int=16000,
            channels:int=1,
            duration:int=5,
    ):
        self.sample_rate=sample_rate
        self.channels=channels
        self.duration=duration

        self.output_dir=Path("asstes/audio")
        self.output_dir.mkdir(parents=True,exist_ok=True)

    def record(self)->str:
        print("\n Listening....")

        recording=sd.rec(
            int(self.duration*self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16",
        )

        sd.wait()

        file_path=self.output_dir/"input.wav"

        write(file_path,self.sample_rate,recording)

        print("Recorded")

        return str(file_path)