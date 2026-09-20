def support_routing():

    print("Past experience case detected.")

    print("1. Certified Counsellor")
    print("2. DLSA Legal Aid")

    choice = input("Select support service: ")

    if choice == "1":
        print("Case routed to Certified Counsellor.")
        return "Counsellor"

    elif choice == "2":
        print("Case routed to DLSA Legal Aid.")
        return "DLSA Legal Aid"

    else:
        print("Invalid choice.")
        return "Invalid"


if __name__ == "__main__":

    result = support_routing()

    print("Support Service:", result)
