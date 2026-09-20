from voice_input import get_voice_input
from speech_to_text import convert_speech_to_text

from nlp.nlp_analysis import analyze_text

from nlp.assessment.distress_severity import (
    calculate_distress_score,
    calculate_severity_score
)

from nlp.assessment.verification.human_verification import (
    human_verification
)

from nlp.assessment.verification.routing.case_routing import (
    route_case
)

from nlp.assessment.verification.routing.emergency.emergency_routing import (
    emergency_routing
)

from nlp.assessment.verification.routing.emergency.support.counselor_legal_aid import (
    support_routing
)


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

    # Step 4: Distress score
    distress_score = calculate_distress_score(text)

    print("\nDistress Score:", distress_score)

    # Step 5: Severity score
    severity = calculate_severity_score(distress_score)

    print("Severity:", severity)

    # Step 6: Human verification
    verified = human_verification(
        distress_score,
        severity
    )

    # Step 7: Routing only after human verification
    if verified:

        case_type = route_case()

        # Active emergency
        if case_type == "emergency":

            emergency_service = emergency_routing()

            print(
                "\nFinal Emergency Service:",
                emergency_service
            )

        # Past experience
        elif case_type == "past_experience":

            support_service = support_routing()

            print(
                "\nFinal Support Service:",
                support_service
            )

        else:

            print("\nInvalid case type.")

    else:

        print("\nCase stopped because human verification failed.")


if __name__ == "__main__":
    main()
