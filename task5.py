# CONTACT BOOK
contacts={}
def add_contact():
    name=input("Enter contact name =")
    phone=int(input("Enter contact phone number ="))
    email=input("Enter contact email =")
    address=input("Enter contact address =")
    contacts[name]={'Phone':phone,'email':email,'address':address}
    print(f"Contact {name} added successfully.")
def update_contact():
    name=input("Enter contact name to update =")
    if name in contacts:
        phone=input("Enter new phone number =")
        email=input("Enter new email =")
        address=input("Enter new address =")
        contacts[name]={'Phone':phone,'email':email,'address':address}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")
def search_contact():
    name=input("Enter contact name to search =")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print(f"Contact {name} not found.")
def view_contact():
    name=input("Enter contact name to view =")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print(f"Contact {name} not found.")
def delete_contact():
    name=input("Enter contact name to delete =")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice=input("Enter your choice 1,2,3,4,5,6: ")
        if choice=='1':
            add_contact()
        elif choice=='2':
            update_contact()
        elif choice=='3':
            search_contact()
        elif choice=='4':
            view_contact()
        elif choice=='5':
            delete_contact()
        elif choice=='6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()