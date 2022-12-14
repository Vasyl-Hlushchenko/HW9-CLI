CONTACTS = {}


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except (ValueError, IndexError, UnboundLocalError):
            print("Error. Give me correct name and phone, please")
        except KeyError:
            print("Error. Enter user name, please")
    return wrapper


def hello_handler():
    print("How can I help you?")


def quit_handler():
    print("Good bye!")
    quit()


@input_error
def change_contact_handler(var):
    name = var.split()[1]
    if (var.split()[2]).isdigit():
        phone = var.split()[2]
    CONTACTS[name] = phone
    print("Contact was changed")


def show_contacts_handler():
    for key, value in CONTACTS.items():
        print(f"{key}: {value}")


@input_error
def add_contact_handler(var):
    if (var.split()[1]).isalpha():
        name = var.split()[1]
    if (var.split()[2]).isdigit():
        phone = var.split()[2]
    CONTACTS[name] = phone
    print(f"New contact was added")


@input_error
def find_contact_handler(var):
    name = var.split()[1]
    print(f"{name}: {CONTACTS[name]}")


COMMANDS = {
    "hello": hello_handler,
    "show all": show_contacts_handler,
    "exit": quit_handler,
    "close": quit_handler,
    "good bye": quit_handler,
}


def main():
    while True:
        var = (input("Enter command: ")).lower()
        if var.startswith('add'):
            add_contact_handler(var)
        elif var.startswith('change'):
            change_contact_handler(var)
        elif var.startswith('phone'):
            find_contact_handler(var)
        elif var not in COMMANDS:
            print("Wrong command!")
            continue
        else:
            COMMANDS[var]()


if __name__ == "__main__":
    main()