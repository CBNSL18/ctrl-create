```python
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the voice.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is not available.")
        return ""


if __name__ == "__main__":
    get_voice_input()
```
