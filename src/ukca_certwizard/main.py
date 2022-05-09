import typer
from typing import Any

from . import bulk
from . import fake_bulk
from . import hostcert
from . import usercert

app = typer.Typer()
app.add_typer(bulk.app, name="bulk")
app.add_typer(fake_bulk.app, name="fake_bulk")
app.add_typer(hostcert.app, name="hostcert")
app.add_typer(usercert.app, name="usercert")


def main() -> Any:
    return app()
