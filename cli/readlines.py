import readline


def load_choices():
    return "Abba Acca CDA DAA".split()


def display_choices(choices):
    print("Select an option:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")


def complete(text, state):
    lower_text = text.lower()

    choices_lower = [choice.lower() for choice in choices]
    options = [choice for choice in choices_lower if choice.startswith(lower_text)]
    if state < len(options):
        return options[state]
    return None


def get_user_choice(choices):
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")

    while True:
        try:
            choice = input("Enter your choice: ")
            if choice in choices:
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    choices = load_choices()
    display_choices(choices)
    selected_choice = get_user_choice(choices)
    print(f"You selected: {selected_choice}")
