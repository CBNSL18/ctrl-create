import speech_recognition as sr


def get_voice_input():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Please speak...")

        audio = recognizer.listen(source)

    audio_file = "input.wav"

    with open(audio_file, "wb") as file:
        file.write(audio.get_wav_data())

    print("Voice recorded successfully.")

    return audio_file


if __name__ == "__main__":

    get_voice_input()



