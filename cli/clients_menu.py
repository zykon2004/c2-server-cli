from db_helper import get_clients
from tasks import send_command
from schema import Command, CommandType
from printer import (
    generate_choice_table,
    goodbye,
    offer_choice,
    rich_print,
    generate_table,
)
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def kill_menu():
    rich_print(":skull: [yellow bold]Kill :skull:")
    menu_items = {"1": "All", "2": "Select Client", "9": "Go Back", "0": "Exit"}
    console = Console()

    while True:
        choice = offer_choice(menu_items)
        match choice:
            case "1":
                send_command(target="all", type=CommandType.KILL)
                rich_print("KILLED `EM ALL! :hammer: :guitar:")
                break

            case "2":
                clients_with_header = get_clients(with_column_names=True)

                if clients := clients_with_header[1:]:
                    choices = [str(i + 1) for i in range(0, len(clients))]
                    table = generate_choice_table(clients_with_header)
                    console.print(table)
                    choice = Prompt.ask("Enter Your Choice", choices=choices)
                    target = clients_with_header[int(choice)][1]
                    send_command(target=target, type=CommandType.KILL)
                    rich_print(f"KILLED {target}")

                else:
                    rich_print(":warning: [red] No living clients found.")
                    break

            case "9":
                break
                # Go back to previous loop
            case "0":
                goodbye()


def client_status():
    rich_print("[yellow bold]Status")
    menu_items = {"9": "Go Back", "0": "Exit"}
    console = Console()

    while True:
        clients_with_header = get_clients(
            with_column_names=True, client_liveliness_threshold=9999
        )
        table = generate_table(clients_with_header)
        console.print(table)
        choice = offer_choice(menu_items)

        match choice:
            case "9":
                break
                # Go back to previous loop
            case "0":
                goodbye()
