import pathlib
import sys
from typing import Optional

import typer
from typing_extensions import Annotated


def _count_metrics(data: bytes) -> dict[str, int]:
    text = data.decode("utf-8", errors="replace")
    return {
        "lines": data.count(b"\n"),
        "words": len(text.split()),
        "chars": len(text),
        "bytes": len(data),
    }


def _read_input(file_path: Optional[str]) -> tuple[bytes, bool]:
    if file_path:
        try:
            return pathlib.Path(file_path).read_bytes(), True
        except FileNotFoundError as exc:
            raise typer.BadParameter(f"File not found: {file_path}", param_hint="file_path") from exc
        except PermissionError as exc:
            raise typer.BadParameter(f"Permission denied: {file_path}", param_hint="file_path") from exc

    return sys.stdin.buffer.read(), False


def _selected_metrics(
    lines: bool,
    words: bool,
    chars: bool,
    bytes_count: bool,
) -> list[str]:
    if not any((lines, words, chars, bytes_count)):
        return ["lines", "words", "bytes"]

    order = ("lines", "words", "chars", "bytes")
    selected = {
        "lines": lines,
        "words": words,
        "chars": chars,
        "bytes": bytes_count,
    }
    return [metric for metric in order if selected[metric]]


def mwc(
    lines: Annotated[
        bool,
        typer.Option("-l", "--lines", help="Count newline characters"),
    ] = False,
    words: Annotated[
        bool,
        typer.Option("-w", "--words", help="Count words"),
    ] = False,
    chars: Annotated[
        bool,
        typer.Option("-m", "--chars", help="Count characters"),
    ] = False,
    bytes_count: Annotated[
        bool,
        typer.Option("-c", "--bytes", help="Count bytes"),
    ] = False,
    file_path: Annotated[
        Optional[str],
        typer.Argument(help="File path. Omit to read from stdin."),
    ] = None,
):
    input_data, from_file = _read_input(file_path)
    metrics = _count_metrics(input_data)
    metric_order = _selected_metrics(lines, words, chars, bytes_count)

    counts = " ".join(str(metrics[name]) for name in metric_order)
    if from_file and file_path:
        print(f"{counts} {file_path}")
        return

    print(counts)
