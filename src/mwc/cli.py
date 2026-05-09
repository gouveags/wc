import typer

from .mwc import mwc


app = typer.Typer()
app.command()(mwc)


if __name__ == "__main__":
    app()
