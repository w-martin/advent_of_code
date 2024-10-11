from pathlib import Path
from typing import Annotated

import typer.core

typer.core.rich = None
from transformer_factory import TransformerFactory


def main(year: Annotated[int, typer.Argument(min=2015, max=2024)],
         day: Annotated[int, typer.Argument(min=1, max=25)],
         part: Annotated[int, typer.Argument(min=1, max=2)]):
    print(f"Running year {year}, day {day}, part {part}")
    transformer = TransformerFactory().new(year=year, day=day)
    data = (Path(__file__).parents[2] / "data" / str(year) / f"day_{day:02d}.txt").read_text()
    match part:
        case 1:
            print(transformer.transform_1(data))
        case 2:
            print(transformer.transform_2(data))


if __name__ == "__main__":
    typer.run(main)
