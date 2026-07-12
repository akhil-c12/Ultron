while True:
    audio=microphone.read()
    probability = model.predict(audio)
    if probability>threshold:
        activate_ultron()


