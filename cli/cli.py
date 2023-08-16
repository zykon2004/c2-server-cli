import random
from datetime import datetime
from time import sleep

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", size=10),
    )

    return layout


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            Text("""<--- Main Menu (Ctrl+C)""", style="bold yellow"),
            Text.assemble(("Server status: ", "bold"), ("UP", "bold green")),
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="italic magenta")


def generate_table() -> Table:
    """Make a new table."""
    table = Table(expand=True)
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}",
            f"{value:3.2f}",
            "[red]ERROR" if value < 50 else "[green]SUCCESS",  # noqa: PLR2004
        )
    return table


layout = make_layout()
layout["header"].update(Header())
layout["main"].update(generate_table())


with Live(layout, refresh_per_second=1, screen=True) as live:
    try:
        while True:
            layout["main"].update(generate_table())
            sleep(3)
    except KeyboardInterrupt:
        live.stop()
        from example import full_example

        full_example()
        # live.update(generate_table())
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
