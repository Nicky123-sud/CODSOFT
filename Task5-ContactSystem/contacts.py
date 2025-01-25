import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name}: {details['phone']}, {details['email']}, {details['address']}")
    else:
        print("\nNo contacts found.")

# Function to search for a contact by name or phone number
def search_contact(contacts, search_term):
    results = {name: details for name, details in contacts.items()
               if search_term.lower() in name.lower() or search_term in details['phone']}
    if results:
        print("\nSearch Results:")
        for name, details in results.items():
            print(f"{name}: {details['phone']}, {details['email']}, {details['address']}")
    else:
        print(f"\nNo contacts found for '{search_term}'.")

# Function to add a new contact
def add_contact(contacts):
    name = input("\nEnter the contact's name: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address: ").strip()

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("\nContact added successfully!")
    save_contacts(contacts)

# Function to update an existing contact
def update_contact(contacts):
    name = input("\nEnter the name of the contact you want to update: ").strip()

    if name in contacts:
        phone = input(f"Enter the new phone number for {name} (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter the new email address for {name} (current: {contacts[name]['email']}): ").strip()
        address = input(f"Enter the new address for {name} (current: {contacts[name]['address']}): ").strip()

        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("\nContact updated successfully!")
        save_contacts(contacts)
    else:
        print(f"\nContact for {name} not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("\nEnter the name of the contact you want to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"\nContact for {name} deleted successfully!")
        save_contacts(contacts)
    else:
        print(f"\nContact for {name} not found.")

# Main function to run the contact management system
def contact_manager():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("\nEnter the name or phone number to search for: ").strip()
            search_contact(contacts, search_term)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("\nContacts saved and exiting.")
            break
        else:
            print("\nInvalid choice. Please select between 1 and 6.")

# Run the contact manager
contact_manager()
