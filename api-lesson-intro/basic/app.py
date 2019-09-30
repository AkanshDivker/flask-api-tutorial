# Basic Python Guestbook App

# A list containing names of guests
guestlist = ["Akansh", "Bill Gates", "Elon Musk"]


# Method to add a new name to our list
def add_name(message: dict):
    guestlist.append(message)


# Print all current names
def print_names():
    print()

    for m in guestlist:
        print(m)

    print()


# Delete a name based on the index in the list
def delete_name(id: int):
    guestlist.pop(id)


# Start our Python program and continue taking input until exit
def start_program():
    end_program = False

    while end_program != True:
        print("1. Sign guestbook")
        print("2. Print names")
        print("3. Delete a name")
        print("4. Exit")

        action = int(input("Select an option: "))

        if action == 1:
            print("")

            name = input("Enter your name: ")
            add_name(name)
        elif action == 2:
            print_names()
        elif action == 3:
            id = int(input("Enter a name ID to delete: "))
            delete_name(id)
        elif action == 4:
            end_program = True
        else:
            continue


if __name__ == "__main__":
    start_program()
