# Certificate Eligibility Project

print("===== Certificate Eligibility Checker =====")

# Asking user about their participation
attendance = input("Did you attend All Day or had a Day Gap? (Type 'All Day' or 'Day Gap'): ")

if attendance.lower() == "all day":
    print("\nYou selected All Day.")
    assignment = input("Did you submit the Assignment? (yes/no): ")
    live_class = input("Did you attend the LIVE Class? (yes/no): ")
    camera = input("Was your Camera On during the class? (yes/no): ")

    if assignment.lower() == "yes" and live_class.lower() == "yes" and camera.lower() == "yes":
        print("\n✅ Congratulations! You are Eligible for the Certificate.")
    else:
        print("\nSorry, you are Not Eligible for the Certificate.")

elif attendance.lower() == "day gap":
    print("\nSorry, you are Not Eligible for the Certificate.")

else:
    print("Invalid input. Please type 'All Day' or 'Day Gap'.")