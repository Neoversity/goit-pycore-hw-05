# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
# Цей декоратор відповідає за повернення користувачеві повідомлень типу 
# "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, 
# що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. 
# оли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. 
# Виконання програми при цьому не припиняється.

# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має власний декоратор input_error, 
# який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
# Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.



def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return None, []
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command. Usage: add [name] [phone]")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_phone(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command. Usage: change [name] [phone]")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"Contact with name '{name}' does not exist.")
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid command. Usage: phone [name]")
    name = args[0]
    if name not in contacts:
        raise KeyError(f"Contact with name '{name}' does not exist.")
    return f"Phone number for {name}: {contacts[name]}"


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    return ""

def show_commands():
    return "Available commands: hello, add, change, phone, all, close, exit"
def main():
    contacts = {}
    print('Welcome to the assistant Contact_Bot!')
    
    while True:
        print(show_commands())  # Друкуємо список команд
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_phone(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))    

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()




# *********************************************************************
# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command:
# *********************************************************************


