# Roadmap Provider Project

print("===== Roadmap Provider Project =====")

# Asking user if Fresher or Experienced
user_type = input("Are you a Fresher or Experienced? (Type 'Fresher' or 'Experienced'): ")

if user_type.lower() == "fresher":
    print("\nYou selected Fresher.")
    print("Choose your path:")
    print("1. Web Development")
    print("2. App Development / DS, ML, AI")
    print("3. DS, ML, AI")

    choice = input("Enter 1 or 2 or 3: ")

    if choice == "1":
        print("\nFresher - Web Development Roadmap:")
        print("Learn HTML, CSS, JS, Python, Django")
    elif choice == "2":
        print("\nFresher - App Dev:")
        print("Learn Java, DSA, Build Projects")
        print("Learn Python, Maths, R")
    elif choice == "3":
        print("\nFresher - DS, ML, AI Roadmap:")
        print("Learn Python, Maths, R")
    else:
        print("Invalid choice.")

elif user_type.lower() == "experienced":
    print("\nYou selected Experienced.")
    print("Choose your path:")
    print("1. Data Analytics")
    print("2. Front end development")
    print("3. Cloud Computing / Front-end")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nExperienced - Data Analytics Roadmap:")
        print("Learn Python, Excel, PowerBI")
    elif choice == "2":
        print("\nExperienced - DevOps & Automation Roadmap:")
        print("Learn DevOps and Python for Automation")
    elif choice == "3":
        print("\nExperienced - Backend Development Roadmap:")
        print("Learn Python and Django for Backend")
    elif choice == "4":
        print("\nExperienced - Cloud/Front-end Roadmap:")
        print("Explore Cloud Computing and Front-end")
    else:
        print("Invalid choice.")

else:
    print("Invalid input. Please type 'Fresher' or 'Experienced'.")