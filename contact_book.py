import json
import logging

# ---------------- LOGGING CONFIG ----------------
logging.basicConfig(
    filename="contact_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Contact Book application started")


# ---------------- FILE OPERATIONS ----------------
def load_contacts():
    """Load contacts from JSON file"""
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("contacts.json file not found, returning empty list")
        return []
    except json.JSONDecodeError:
        logging.error("JSON file is corrupted")
        return []


def save_contacts(contacts):
    """Save contacts to JSON file"""
    try:
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        logging.error(f"Failed to save contacts: {e}")


# ---------------- CONTACT FEATURES ----------------
def add_contact():
    """Add a new contact"""
    try:
        name = input("Enter name: ")
        phone = input("Enter mobile number: ")

        contacts = load_contacts()

        contacts.append({
            "name": name,
            "phone": phone
        })

        save_contacts(contacts)

        logging.info(f"New contact added: {name}")
        print(" Contact saved successfully!")

    except Exception as e:
        logging.error(f"Error while adding contact: {e}")
        print(" Something went wrong while adding contact")


def show_contacts():
    """Display all contacts"""
    try:
        contacts = load_contacts()

        if not contacts:
            logging.warning("No contacts found")
            print(" No contacts found!")
            return

        print("\n --- Contact List ---")
        for c in contacts:
            print(f"Name: {c['name']} | Phone: {c['phone']}")
        print("----------------------")

        logging.info("Contacts displayed successfully")

    except Exception as e:
        logging.error(f"Error while showing contacts: {e}")
        print(" Error while displaying contacts")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n --- Contact Book ---")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            logging.info("User selected: Add Contact")
            add_contact()

        elif choice == "2":
            logging.info("User selected: Show Contacts")
            show_contacts()

        elif choice == "3":
            logging.info("User exited the application")
            print(" Goodbye!")
            break

        else:
            logging.warning("User entered invalid choice")
            print(" Invalid choice! Try again.")


# ---------------- PROGRAM START ----------------
if __name__ == "__main__":
    main()
