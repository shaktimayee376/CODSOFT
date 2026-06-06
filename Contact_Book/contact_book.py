contacts = []

def add_contact():
    person = {}

    person["name"] = input("Enter Name: ")
    person["phone"] = input("Enter Phone Number: ")
    person["email"] = input("Enter Email: ")
    person["address"] = input("Enter Address: ")

    contacts.append(person)
    print("Contact Added Successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No Contacts Available")
        return

    print("\nCONTACT LIST")
    for index, person in enumerate(contacts, start=1):
        print(f"{index}. {person['name']} - {person['phone']}")

def search_contact():
    keyword = input("Enter Name or Phone: ").lower()

    found = False

    for person in contacts:
        if keyword in person["name"].lower() or keyword in person["phone"]:
            print("\nContact Found")
            print("Name:", person["name"])
            print("Phone:", person["phone"])
            print("Email:", person["email"])
            print("Address:", person["address"])
            found = True

    if not found:
        print("Contact Not Found")

def update_contact():
    target = input("Enter Contact Name: ").lower()

    for person in contacts:
        if person["name"].lower() == target:

            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            person["phone"] = new_phone
            person["email"] = new_email
            person["address"] = new_address

            print("Contact Updated")
            return

    print("Contact Not Found")
def delete_contact():
    target = input("Enter Contact Name: ").lower()
    for person in contacts:
        if person["name"].lower() == target:
            contacts.remove(person)
            print("Contact Deleted")
            return
    print("Contact Not Found")
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    option = input("Choose Option: ")
    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        update_contact()
    elif option == "5":
        delete_contact()
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")