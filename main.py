from nlp.assessment.distress_severity import (
    calculate_distress_score,
    calculate_severity_score
)

from nlp.assessment.verification.human_verification import human_verification

from nlp.assessment.verification.routing.case_routing import route_case

from nlp.assessment.verification.routing.emergency.emergency_routing import emergency_routing

from nlp.assessment.verification.routing.emergency.support.counselor_legal_aid import support_routing


def main():

    print("===== CTRL-CREATE =====")

    text = input("Enter the reported text: ")

    distress_score = calculate_distress_score(text)

    severity = calculate_severity_score(distress_score)

    print("\nDistress Score:", distress_score)
    print("Severity:", severity)

    verified = human_verification(distress_score, severity)

    if verified:

        case_type = route_case()

        if case_type == "emergency":

            emergency_routing()

        elif case_type == "past_experience":

            support_routing()

    else:

        print("Case was not verified.")


if __name__ == "__main__":
    main()
