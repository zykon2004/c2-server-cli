import sys
from typing import Any, Dict, List

from rich import print as rich_print
from rich.prompt import Prompt
from rich.table import Table


def goodbye():
    rich_print("[bold green]Goodbye :palm_tree:")
    sys.exit(0)


def offer_choice(menu_items: Dict[str, str]) -> str:
    for key, value in menu_items.items():
        rich_print(f"({key}) {value}")

    return Prompt.ask("Enter Your Choice", choices=list(menu_items.keys()))


def generate_table(content_with_header: List[Any]):
    table = Table(expand=True)
    for column in content_with_header[0]:
        table.add_column(column)
    for row in content_with_header[1:]:
        table.add_row(*row.values(stringify=True))
    return table


def generate_choice_table(content_with_header: List[Any]):
    table = Table(expand=True)
    content_with_header[0] = ("choice", *content_with_header[0])
    for column in content_with_header[0]:
        table.add_column(column)
    for index, row in enumerate(content_with_header[1:], start=1):
        table.add_row(str(index), *row.values(stringify=True))
    return table
