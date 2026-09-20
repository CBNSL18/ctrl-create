def calculate_distress_score(text):
    distress_words = [
        "help",
        "scared",
        "afraid",
        "panic",
        "threat",
        "danger",
        "hurt",
        "fear"
    ]

    count = 0

    text = text.lower()

    for word in distress_words:
        if word in text:
            count = count + 1

    distress_score = count * 10

    if distress_score > 100:
        distress_score = 100

    return distress_score


def calculate_severity_score(distress_score):

    if distress_score >= 70:
        severity = "High"

    elif distress_score >= 40:
        severity = "Medium"

    else:
        severity = "Low"

    return severity


if __name__ == "__main__":

    text = input("Enter the text: ")

    distress_score = calculate_distress_score(text)

    severity = calculate_severity_score(distress_score)

    print("Distress Score:", distress_score)

    print("Severity:", severity)
