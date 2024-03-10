def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "\n Invalid arguments for add command. \n Give me a name and phone please."
        except KeyError:
            return "\n Contact not found."
        except IndexError:
            return "\n Incomplete command.  \n Enter corect user name.\n"

    return inner

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name.lower()] = (name, phone)
        return "Contact added."
    else:
        raise ValueError


def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name.lower() in contacts:
            contacts[name.lower()] = (name, phone)
            return "Contact updated."
        else:
            return "Contact not found."
    elif len(args) == 1:
        return "\n Invalid arguments for change command. \n Please provide both name and phone number.\n For example, use: change Eddy 333777 \n"
    else:
        return "Invalid arguments for change command."


@input_error
def delete_contact(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name.lower() in contacts:
            del contacts[name.lower()]
            return "Contact deleted."
        else:
            raise IndexError  
    else:
        return "\n Invalid arguments for delete command. \n Please provide the name of the contact to delete.\nad"

 
@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0].lower()  # Переведення введеного імені до нижнього регістру
        if name in contacts:
            return contacts[name][1]
        else:
            raise KeyError
    else:
        return "Invalid arguments for phone command."


def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, (name, phone) in contacts.items()]) 
    else:
        return "No contacts available."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["good bye","close", "exit", "q", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print()
            print("Unknown command. Available commands are: \n hello, add, change, phone, all, delete, close, exit")
            print()
            print("Available commands:")
            print("hello                      -- to get assistance") 
            print("add NAME PHONE             -- to add a contact") 
            print("change NAME PHONE          -- to change a contact's phone number") 
            print("phone NAME                 -- to get a contact's phone number") 
            print("delete NAME                -- to delete a contact") 
            print("all                        -- to show all contacts") 
            print("q/good bye/close/exit/quit -- to exit the assistant")
            print()

if __name__ == "__main__":
    main()