from clients_menu import client_status, kill_menu
from command_menu import command_status, send_command_menu
from logger import setup_logger
from printer import goodbye, offer_choice, rich_print
from server_status import server_status


def main_menu():
    menu_items = {"1": "Server Status", "2": "Clients", "3": "Commands", "q": "Quit"}
    try:
        while True:
            rich_print(":deciduous_tree: [bold yellow]Main Menu :deciduous_tree:")
            choice = offer_choice(menu_items)
            match choice:
                case "1":
                    server_status()
                case "2":
                    client_menu()
                case "3":
                    command_menu()
                case "q":
                    goodbye()

    except KeyboardInterrupt:
        goodbye()


def client_menu():
    menu_items = {"1": "Status", "2": "Kill", "b": "Go Back", "q": "Quit"}
    while True:
        rich_print("[yellow bold]Clients Menu")
        choice = offer_choice(menu_items)
        match choice:
            case "1":
                client_status()
            case "2":
                kill_menu()
            case "b":
                break
            case "q":
                goodbye()


def command_menu():
    menu_items = {"1": "Status", "2": "Send Command", "b": "Go Back", "q": "Quit"}
    while True:
        rich_print("[yellow bold]Commands Menu")
        choice = offer_choice(menu_items)
        match choice:
            case "1":
                command_status()
            case "2":
                send_command_menu()
            case "b":
                break
            case "q":
                goodbye()


if __name__ == "__main__":
    rich_print("Welcome! :mage: ")
    setup_logger("c2-server-cli")
    main_menu()
"""
Main Menu:
    Server Status
    Client
        Status
        Kill
    Command
        Send Command
            Choose: Client, All
            Choose: Payload
            Input: Args (separated by space)
        View Status
"""
