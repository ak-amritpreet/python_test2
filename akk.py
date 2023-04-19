phoneDirectory = {}

def add_record():
    name = input("Enter name = ")
    phone_number = input("Enter phone number = ")
    phoneDirectory[name] = phone_number
    print("RECORD ADDED")

def search_record():
    name = input("Enter name = ")
    if name in phoneDirectory:
        print(name + ": " + phoneDirectory[name])
    else:
        print("Record not found!")

def update_record():
    name = input("Enter name = ")
    if name in phoneDirectory:
        PHONE_NUMBER = input("Enter new phone number = ")
        phoneDirectory[name] = PHONE_NUMBER
        print("Record updated")
    else:
        print("Record not found!")

def delete_record():
    name = input("Enter name = ")
    if name in phoneDirectory:
        del phoneDirectory[name]
        print("Record deleted")
    else:
        print("Record not found!")

print("WELCOME TO THE GRANN'S PHONE DIRECTORY\n")
while True:
    print("1. ADD A RECORD")
    print("2. SEARCH A RECORD")
    print("3. UPDATE A RECORD")
    print("4. DELETE A RECORD")
    print("5. QUIT")

    choice = input("Enter your choice = ")

    if choice == '1':
        add_record()
    elif choice == '2':
        search_record()
    elif choice == '3':
        update_record()
    elif choice == '4':
        delete_record()
    elif choice == '5':
        print("EXITING THE PROGRAM...")
        break
    else:
        print("INVALID CHOICE....PLEASE TRY AGAIN\n")