from transformers import pipeline


transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3"
)


def convert_speech_to_text(audio_file):

    result = transcriber(audio_file)

    text = result["text"]

    print("Converted Text:", text)

    return text
