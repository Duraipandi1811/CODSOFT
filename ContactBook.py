class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact['name'] or search_term in contact['phone']]
        if not results:
            print("No matching contacts found.")
        else:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, search_term, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
                print(f"Contact {new_name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.contacts.remove(contact)
                print(f"Contact {contact['name']} deleted successfully!")
                return
        print("Contact not found.")

def main():
    book = ContactBook() 
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            book.update_contact(search_term, new_name, new_phone, new_email, new_address)

        elif choice == '5':
            search_term = input("Enter name or phone number of the contact to delete: ")
            book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
