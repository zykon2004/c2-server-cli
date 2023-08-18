from time import sleep

from db_helper import get_clients
from printer import generate_table
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from settings import STATUS_REFRESH_INTERVAL_SECONDS
from tasks import check_server_status


def generate_table_of_living_clients() -> Table:
    client_list_with_header = get_clients(with_column_names=True)
    return generate_table(client_list_with_header)


def server_status() -> None:
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
            status_text = (
                ("UP", "bold green") if check_server_status() else ("DOWN", "bold red")
            )
            grid = Table.grid(expand=True)
            grid.add_column(justify="left", ratio=1)
            grid.add_column(justify="center", ratio=1)
            grid.add_column(justify="right", ratio=1)
            grid.add_row(
                Text("""<--- Main Menu (Ctrl+C)""", style="bold yellow"),
                Text.assemble(("Server status: ", "bold"), status_text),
                Text(
                    f"Refresh interval: {STATUS_REFRESH_INTERVAL_SECONDS}sec",
                    style="yellow",
                ),
            )
            return Panel(grid, style="italic magenta")

    layout = make_layout()
    layout["header"].update(Header())
    layout["main"].update(generate_table_of_living_clients())

    with Live(layout, auto_refresh=False, screen=True) as live:
        try:
            while True:
                layout["main"].update(generate_table_of_living_clients())
                sleep(STATUS_REFRESH_INTERVAL_SECONDS)
                live.refresh()
        except KeyboardInterrupt:
            live.stop()
