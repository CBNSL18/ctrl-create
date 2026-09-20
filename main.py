from voice_input import get_voice_input
from speech_to_text import convert_speech_to_text


def main():

    print("===== CTRL-CREATE =====")

    # Voice record karna
    audio_file = get_voice_input()

    # Voice ko text mein convert karna
    text = convert_speech_to_text(audio_file)

    print("\nFinal Text:", text)


if __name__ == "__main__":
    main()
