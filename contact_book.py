contacts={}
def add_contact(name,phone,email,address):
    contacts[name]={
        'phone':phone,
        'email':email,
        'address':address
    }
    print(f"Contact {name} added succesfully")
def view_contacts():
    if not contacts:
        print("There are no contacts")
    else:
        for name,details in contacts.items():
            print(f"\nName: {name}\nphone number: {details['phone']}\nemail address: {details['email']}\naddress: {details['address']}\n")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully")
    else:
        print("Contact not found")
def update_contact(name,phone=None,email=None,address=None):
    if name in contacts:
        if phone:
            contacts[name]['phone']=phone
        if email:
            contacts[name]['email']=email
        if address:
            contacts[name]['address']=address
        print(f"Contact {name} updated successfully")
    else:
        print("Contact not found")
def search_contact(search):
    results = []
    search = search.lower()
    for name, details in contacts.items():
        if search in name.lower():
            results.append((name, details))
    if results:
        print("Contact found\n")
        for name, details in results:
            print(f"Name: {name}\nphone number: {details['phone']}\nemail: {details['email']}\naddress: {details['address']}\n")
    else:
        print("No contacts found")

def display():
    print("Contact Book")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. View Contacts list")
    print("5. Search Contact")
    print("6. Exit")
def main():
    display()
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif user_choice == '2':
            name = input("Enter name: ")
            delete_contact(name)
        elif user_choice == '3':
            name = input("Enter the name of the contact to be updated: ")
            phone = input("Enter the phone number of the contact to be updated: ")
            email = input("Enter the email of the contact to be updated: ")
            address = input("Enter the address of the contact to be updated: ")
            update_contact(name, phone, email, address)
        elif user_choice == '4':
            view_contacts()
        elif user_choice == '5':
            search_term = input("Enter name to search: ")
            search_contact(search_term)
        elif user_choice == '6':
            exit()
        else:
            print("Choose from the above options only")

if __name__=="__main__":
    main()