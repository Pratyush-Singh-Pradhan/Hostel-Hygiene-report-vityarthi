import json
from datetime import datetime
import os


# I'm using a JSON file just because it's simple and doesn't need any setup.
DATA_FILE = "complaints.json"

# Define the issue categories once for use in both display and lookup
ISSUE_CATEGORIES = {
    "1": "Washroom",
    "2": "Room",
    "3": "Corridor",
    "4": "Water Cooler",
    "5": "Dustbin",
    "6": "Other"
}


def load_data():
    """Load the already stored complaints, if the file exists."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError):
        # If the file is empty, corrupted, or cannot be read, return an empty list instead of crashing
        print(f"Warning: Could not read or decode {DATA_FILE}. Starting with an empty list.")
        return []


def save_data(all_data):
    """Save the updated list of complaints back into the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(all_data, file, indent=4)
    except IOError:
        print(f"Error: Could not write data to {DATA_FILE}.")


def display_issue_options():
    """Helper function to display the issue category menu."""
    print("\nChoose the issue category:")
    for key, value in ISSUE_CATEGORIES.items():
        print(f"{key}. {value}")


def submit_complaint():
    print("\n--- New Hygiene Complaint ---\n")

    # Collect basic details
    name = input("Your Name: ")
    reg = input("Registration Number: ")
    gender = input("Gender (boy/girl): ").strip().lower()
    block = input("Hostel Block: ")

    # --- Input Validation for Issue Category ---
    while True:
        display_issue_options() # Display options before input
        
        issue_pick = input("Pick an option (1-6): ").strip()
        
        if issue_pick in ISSUE_CATEGORIES:
            issue = ISSUE_CATEGORIES[issue_pick]
            break # Exit the loop if input is valid
        else:
            print("\n*** Invalid option selected. Please pick a number from 1 to 6. ***")
    # --- End Input Validation ---

    # Display the final choice to the user before moving on
    print(f"\nIssue selected: **{issue}**") 
    
    desc = input("\nDescribe the problem:\n")

    all_data = load_data()

    all_data.append({
        "name": name,
        "reg": reg,
        "gender": gender,
        "block": block,
        "issue": issue,
        "description": desc,
        "submitted_at": str(datetime.now())
    })

    save_data(all_data)
    print("\nYour complaint has been recorded.\n")


def view_all():
    """Admin view: show every complaint submitted so far."""
    print("\n--- All Recorded Complaints ---\n")
    all_data = load_data()

    if not all_data:
        print("No complaints have been logged yet.\n")
        return

    # To show the most recent complaint first
    all_data.reverse() 

    for i, entry in enumerate(all_data, 1):
        print(f"--- Complaint #{i} ---")
        print(f"Name: {entry['name']}")
        print(f"Reg No: {entry['reg']}")
        print(f"Gender: {entry['gender']}")
        print(f"Hostel Block: {entry['block']}")
        print(f"Issue Type: **{entry['issue']}**")
        print("Description:", entry['description'])
        print("Filed On:", entry['submitted_at'])
        print("--------------------------\n")


def main():
    while True:
        print("\n=== 🏠 Hostel Hygiene Reporting ===")
        print("1. Submit a complaint")
        print("2. Admin: View all complaints")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            submit_complaint()
        elif choice == "2":
            view_all()
        elif choice == "3":
            print("\nExiting... take care!")
            break
        else:
            print("\n*** Invalid choice, please enter 1, 2, or 3. ***\n")


if __name__ == "__main__":
    main()