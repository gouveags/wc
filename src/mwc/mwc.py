import typer
import os
from typing_extensions import Annotated


def mwc(
    bytes: Annotated[bool, typer.Option(help="Option to count the number of bytes of the given file")] = False,
    file_path: Annotated[str, typer.Argument(help="File path")] = "",
):
    if bytes:
        size = os.path.getsize(file_path)
        print(f"{size} {file_path}")
