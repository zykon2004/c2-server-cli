from db_helper import get_clients
from printer import (
    generate_choice_table,
    generate_table,
    goodbye,
    offer_choice,
    rich_print,
)
from rich.console import Console
from rich.prompt import Prompt
from schema import CommandType
from tasks import send_command


def kill_menu():
    rich_print(":skull: [yellow bold]Kill :skull:")
    menu_items = {"1": "All", "2": "Select Client", "b": "Go Back", "q": "Quit"}
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
                    table = generate_choice_table(clients_with_header)
                    console.print(table)
                    choices = [str(i + 1) for i in range(0, len(clients))]
                    choices.extend(["b", "q"])
                    choice = Prompt.ask("Enter Your Choice", choices=choices)
                    match choice:
                        case "b":
                            break
                            # Go back to previous loop
                        case "q":
                            goodbye()

                    target = clients[int(choice) - 1].id
                    send_command(target=target, type=CommandType.KILL)
                    rich_print(f"KILLED {target}")

                else:
                    rich_print(":warning: [red] NO LIVING CLIENTS FOUND.")
                    break

            case "b":
                break
                # Go back to previous loop
            case "q":
                goodbye()


def client_status():
    rich_print("[yellow bold]Client Status")
    menu_items = {"b": "Go Back", "q": "Quit"}
    console = Console()

    while True:
        clients_with_header = get_clients(
            with_column_names=True, client_liveliness_threshold=9999
        )
        table = generate_table(clients_with_header)
        console.print(table)
        choice = offer_choice(menu_items)

        match choice:
            case "b":
                break
                # Go back to previous loop
            case "q":
                goodbye()
