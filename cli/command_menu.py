from db_helper import get_all_payload, get_clients, get_commands
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

console = Console()


def command_status():
    rich_print("[yellow bold]Command Status")
    menu_items = {"b": "Go Back", "q": "Quit"}
    while True:
        commands_with_header = get_commands(with_column_names=True)
        table = generate_table(commands_with_header)
        console.print(table)
        choice = offer_choice(menu_items)

        match choice:
            case "b":
                break
                # Go back to previous loop
            case "q":
                goodbye()


def send_command_menu():
    while True:
        rich_print("[yellow bold]Send Command")
        # 1st Part - Select Client
        clients_with_header = get_clients(with_column_names=True)

        if clients := clients_with_header[1:]:
            table = generate_choice_table(clients_with_header)
            console.print(table)
            choices = [str(i + 1) for i in range(0, len(clients))]
            choices = ["all", *choices, "b", "q"]
            choice = Prompt.ask("Enter Your Choice", choices=choices)
            match choice:
                case "all":
                    target = "all"
                case "b":
                    break
                    # Go back to previous loop
                case "q":
                    goodbye()
                case _:
                    target = clients[int(choice) - 1].id

        else:
            rich_print(":warning: [red bold]NO LIVING CLIENTS FOUND")
            break
        # 2nd Part - Select Payload
        payload_with_header = get_all_payload(with_column_names=True)
        if payloads := payload_with_header[1:]:
            table = generate_choice_table(payload_with_header)
            console.print(table)
            choices = [str(i + 1) for i in range(0, len(payloads))]
            choices = [*choices, "b", "q"]
            choice = Prompt.ask("Enter Your Choice", choices=choices)
            match choice:
                case "b":
                    break
                    # Go back to previous loop
                case "q":
                    goodbye()
                case _:
                    # 1 is the payload id
                    payload_id = payload_with_header[int(choice)].id
                    payload_default_args = payload_with_header[
                        int(choice)
                    ].default_arguments
                    # 3nd Part - Input payload args
                    payload_args = Prompt.ask(
                        "Input payload args:", default=payload_default_args
                    )

                    send_command(
                        target=target,
                        type=CommandType.RUN,
                        payload_id=payload_id,
                        payload_args=payload_args,
                    )
        else:
            rich_print(":warning: [red bold]NO PAYLOADS FOUND")
            break

        match choice:
            case "b":
                break
                # Go back to previous loop
            case "q":
                goodbye()
