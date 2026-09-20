def human_verification(distress_score, severity):

    print("Distress Score:", distress_score)
    print("Severity:", severity)

    print("\nHuman Verification Required")

    decision = input("Enter verification result (yes/no): ")

    if decision.lower() == "yes":
        print("Case verified by human.")
        return True

    else:
        print("Case not verified.")
        return False


if __name__ == "__main__":

    distress_score = int(input("Enter distress score: "))
    severity = input("Enter severity: ")

    result = human_verification(distress_score, severity)

    print("Verification Result:", result)
