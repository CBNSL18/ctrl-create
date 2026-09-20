def emergency_routing():

    print("Emergency routing started.")

    print("1. Police")
    print("2. Fire Service")
    print("3. Ambulance")

    choice = input("Select emergency service: ")

    if choice == "1":
        print("Case routed to Police.")
        return "Police"

    elif choice == "2":
        print("Case routed to Fire Service.")
        return "Fire Service"

    elif choice == "3":
        print("Case routed to Ambulance.")
        return "Ambulance"

    else:
        print("Invalid choice.")
        return "Invalid"


if __name__ == "__main__":

    result = emergency_routing()

    print("Emergency Service:", result)
