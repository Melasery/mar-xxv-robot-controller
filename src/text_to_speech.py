from gtts import gTTS
import pygame
import os

def speak_text(text):
    try:
        tts = gTTS(text)
        tts.save("speech.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        os.remove("speech.mp3")
        return {"message": "OK"}
    except Exception as e:
        return {"error": str(e)}
