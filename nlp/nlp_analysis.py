from transformers import pipeline


# NLP model
classifier = pipeline(
    "text-classification",
    model="google-bert/bert-base-multilingual-cased"
)


def analyze_text(text):
    result = classifier(text)

    print("NLP Result:", result)

    return result


if __name__ == "__main__":
    text = input("Enter the text: ")

    analyze_text(text)
