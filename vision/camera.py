import cv2
import time


class Camera:
    def __init__(self,camera_index:int=0):
        self.camera_index=camera_index

    def capture_frame(self):
        cap=cv2.VideoCapture(self.camera_index)

        if not cap.isOpened():
            raise RuntimeError("Unable to open webcam")

        time.sleep(0.5)

        success,frame=cap.read()

        cap.release()
        if not success:
            raise RuntimeError("Failed to Capture image")

        return frame

    def save_frame(self,filepath:str):
        frame =self.capture_frame()
        cv2.imwrite(filepath,frame)

        return filepath

    def capture_image(self, filepath:str="assets/capture.jpg")->str:
        from pathlib import Path
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        return self.save_frame(filepath)


