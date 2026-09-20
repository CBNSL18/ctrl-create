```python
from transformers import pipeline


# Hugging Face Speech-to-Text model
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3"
)


def convert_speech_to_text(audio_file):
    result = transcriber(audio_file)

    text = result["text"]

    print("Converted Text:", text)

    return text


if __name__ == "__main__":
    audio_file = input("Enter the audio file path: ")

    convert_speech_to_text(audio_file)
```
