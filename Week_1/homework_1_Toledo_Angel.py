import datetime

# Create a contact dictionary from user input
def create_contact():
    print("Enter contact details:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone number: ")

    if first_name == "" or last_name == "" or phone == "":
        print("First name, last name, and phone are required.")
        return None

    email = input("Email (optional): ")
    category = input("Category (personal/work/family): ")
    notes = input("Notes (optional): ")

    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip code: ")

    today = str(datetime.date.today())

    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email,
        'address': {
            'street': street,
            'city': city,
            'state': state,
            'zip_code': zip_code
        },
        'category': category,
        'notes': notes,
        'created_date': today,
        'last_modified': today
    }

    return contact

# Add a contact to the database
def add_contact(contacts_db, contact_data):
    if contact_data is None:
        return None
    contact_id = "contact_" + str(len(contacts_db) + 1)
    contacts_db[contact_id] = contact_data
    return contact_id

# Show one contact's details
def display_contact(contacts_db, contact_id):
    if contact_id in contacts_db:
        contact = contacts_db[contact_id]
        print("\nContact ID:", contact_id)
        print("Name:", contact['first_name'], contact['last_name'])
        print("Phone:", contact['phone'])
        print("Email:", contact['email'])
        print("Category:", contact['category'])
        print("Notes:", contact['notes'])
        print("Address:", contact['address']['street'], contact['address']['city'],
              contact['address']['state'], contact['address']['zip_code'])
        print("Created:", contact['created_date'])
        print("Last Modified:", contact['last_modified'])
        return True
    else:
        print("Contact not found.")
        return False

# List all contacts briefly
def list_all_contacts(contacts_db):
    print("\nAll Contacts:")
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        print(contact_id, "-", contact['first_name'], contact['last_name'], "-", contact['phone'])

# Search by name
def search_contacts_by_name(contacts_db, search_term):
    results = {}
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        if search_term.lower() in contact['first_name'].lower() or search_term.lower() in contact['last_name'].lower():
            results[contact_id] = contact
    return results

# Search by category
def search_contacts_by_category(contacts_db, category):
    results = {}
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        if contact['category'].lower() == category.lower():
            results[contact_id] = contact
    return results

# Find by phone number
def find_contact_by_phone(contacts_db, phone_number):
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        if contact['phone'] == phone_number:
            return contact_id, contact
    return None, None

# Update a contact
def update_contact(contacts_db, contact_id, field_updates):
    if contact_id in contacts_db:
        contact = contacts_db[contact_id]
        for field in field_updates:
            contact[field] = field_updates[field]
        contact['last_modified'] = str(datetime.date.today())
        return True
    else:
        return False

# Delete a contact
def delete_contact(contacts_db, contact_id):
    if contact_id in contacts_db:
        del contacts_db[contact_id]
        return True
    else:
        return False

# Main menu loop
def main_menu():
    contacts_db = {}

    while True:
        print("\nContact Manager Menu:")
        print("1. Add new contact")
        print("2. Search contacts by name")
        print("3. List all contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            contact = create_contact()
            contact_id = add_contact(contacts_db, contact)
            if contact_id:
                print("Contact added with ID:", contact_id)

        elif choice == "2":
            term = input("Enter name to search: ")
            results = search_contacts_by_name(contacts_db, term)
            for cid in results:
                display_contact(contacts_db, cid)

        elif choice == "3":
            list_all_contacts(contacts_db)

        elif choice == "4":
            cid = input("Enter contact ID to update: ")
            field = input("Which field to update (e.g., phone, email): ")
            value = input("New value: ")
            success = update_contact(contacts_db, cid, {field: value})
            if success:
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif choice == "5":
            cid = input("Enter contact ID to delete: ")
            success = delete_contact(contacts_db, cid)
            if success:
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
