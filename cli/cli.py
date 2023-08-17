# import subprocess
# from pathlib import Path
# from subprocess import PIPE, Popen
# from typing import Any, Iterable

# gum = str((Path(__file__).parents[1] / "bin" / "gum").absolute())
# p1 = Popen(["ip", "a"], stdout=PIPE)
# p2 = Popen(["sed", "/^$/d"], stdin=p1.stdout, stdout=PIPE)
# p3 = Popen(["awk", "NR > 1 { print $2 }"], stdin=p2.stdout, stdout=PIPE)
# p4 = Popen(f"{gum} filter".split(), stdin=p3.stdout, stdout=PIPE, text=True)
# stdout, _ = p4.communicate()
# print(stdout)


# def run_command(args: Iterable[str]) -> Any:
#     result = subprocess.run([*args], stdout=subprocess.PIPE, text=True)
#     return result.stdout.split()


# # run_command(f'{gum} spin --spinner dot --title "Buying Bubble Gum..." -- sleep 5'.split())
# print("What's your favorite language?")

from server_status import server_status
from clients_menu import kill_menu, client_status
from printer import goodbye, offer_choice, rich_print
from logger import setup_logger


def main_menu():
    menu_items = {"1": "Server Status", "2": "Clients", "3": "Commands", "0": "Exit"}
    try:
        while True:
            rich_print("[bold yellow]Main Menu")
            choice = offer_choice(menu_items)
            match choice:
                case "1":
                    server_status()
                case "2":
                    client_menu()
                case "3":
                    command_menu()
                case "0":
                    goodbye()

    except KeyboardInterrupt:
        goodbye()


def client_menu():
    menu_items = {"1": "Status", "2": "Kill", "9": "Go Back", "0": "Exit"}
    while True:
        rich_print("[yellow bold]Clients")
        choice = offer_choice(menu_items)
        match choice:
            case "1":
                client_status()
            case "2":
                kill_menu()
            case "9":
                break
                # Go back to main menu's loop
            case "0":
                goodbye()


def command_menu():
    rich_print("[yellow bold]Commands")


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
