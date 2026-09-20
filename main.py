from voice_input import get_voice_input
from speech_to_text import convert_speech_to_text
from nlp.nlp_analysis import analyze_text


def main():

    print("===== CTRL-CREATE =====")

    # Step 1: Voice input
    audio_file = get_voice_input()

    # Step 2: Speech to text
    text = convert_speech_to_text(audio_file)

    print("\nFinal Text:", text)

    # Step 3: NLP analysis
    result = analyze_text(text)

    print("\nNLP Result:", result)


if __name__ == "__main__":
    main()
