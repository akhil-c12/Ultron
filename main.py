from wakeword.wake_detector import WakeWordDetector

def main():
    detector=WakeWordDetector()

    while True:
        wakeword=detector.listen()

        print("===================================")
        print("Ultron Activated!")
        print(f"Detected: {wakeword}")
        print("===================================")

if __name__=="__main__":
    main()


    