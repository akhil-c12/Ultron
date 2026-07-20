import collections
from pathlib import Path

import numpy as np
import sounddevice as sd
import webrtcvad
from scipy.io.wavfile import write


class Recorder:

    def __init__(
            self,
            sample_rate:int=16000,
            channels:int=1,
            frame_duration:int=30,
            aggressiveness:int=2,
            silence_timeout:float=1.0,
            max_record_time:float=30.0,
    ):
        self.sample_rate=sample_rate
        self.channels=channels
        self.frame_duration=frame_duration
        self.aggressiveness=aggressiveness
        self.silence_timeout=silence_timeout
        self.max_record_time=max_record_time
        self.frame_size = int(self.sample_rate * self.frame_duration / 1000)

        self.vad=webrtcvad.Vad(aggressiveness)
        self.audio_buffer=collections.deque()

        self.output_dir=Path("assets/audio")
        self.output_dir.mkdir(parents=True,exist_ok=True)


    def record(self)->str:
        print("\n Listening....")
        frames=[]
        speech_started=False
        silence_frames=0
        max_silence_frames=int(
            self.silence_timeout*1000/self.frame_duration
        )
        max_frames=int(
            self.max_record_time*1000/self.frame_duration
        )
        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16",
            blocksize=self.frame_size,
        ) as stream:

            while True:

                audio, _ = stream.read(self.frame_size)

                audio_bytes = audio.tobytes()

                is_speech = self.vad.is_speech(
                    audio_bytes,
                    self.sample_rate,
                )

                if not speech_started:

                    if is_speech:
                        print(" Voice detected.")
                        speech_started = True
                        frames.append(audio.copy())

                    continue

                frames.append(audio.copy())

                if is_speech:
                    silence_frames = 0
                else:
                    silence_frames += 1

                if silence_frames >= max_silence_frames:
                    print("Silence detected.")
                    break

                if len(frames) >= max_frames:
                    print("⏱ Maximum recording duration reached.")
                    break

        recording = np.concatenate(frames, axis=0)

        file_path = self.output_dir / "input.wav"

        write(file_path, self.sample_rate, recording)

        print("Recording saved.")

        return str(file_path)