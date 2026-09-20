def route_case():

    print("Select the type of case:")

    print("1. Active Emergency")
    print("2. Past Experience")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Active emergency detected.")
        return "emergency"

    elif choice == "2":
        print("Past experience detected.")
        return "past_experience"

    else:
        print("Invalid choice.")
        return "invalid"


if __name__ == "__main__":

    result = route_case()

    print("Case Routing:", result)
