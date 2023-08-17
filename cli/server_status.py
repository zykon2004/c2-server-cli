from datetime import datetime
from time import sleep

from db_helper import get_active_clients
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from settings import STATUS_REFRESH_INTERVAL


def server_status():
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
        client_list_with_header = get_active_clients(with_column_names=True)
        for column in client_list_with_header[0]:
            table.add_column(column)
        for row in client_list_with_header[1:]:
            table.add_row(str(row))
        return table

    layout = make_layout()
    layout["header"].update(Header())
    layout["main"].update(generate_table())

    with Live(layout, refresh_per_second=1, screen=True) as live:
        try:
            while True:
                layout["main"].update(generate_table())
                sleep(STATUS_REFRESH_INTERVAL)
        except KeyboardInterrupt:
            live.stop()

    return server_status()
