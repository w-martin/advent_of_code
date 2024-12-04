from pathlib import Path
from typing import Annotated

import typer.core

typer.core.rich = None
from solver_factory import SolverFactory


def main(year: Annotated[int, typer.Argument(min=2015, max=2024)],
         day: Annotated[int, typer.Argument(min=1, max=25)],
         part: Annotated[int, typer.Argument(min=1, max=2)]):
    print(f"Running year {year}, day {day}, part {part}")
    solver = SolverFactory().new(year=year, day=day)
    data = (Path(__file__).parents[2] / "data" / str(year) / f"day_{day:02d}.txt").read_text()
    match part:
        case 1:
            print(solver.solve_part_1(data))
        case 2:
            print(solver.solve_part_2(data))


if __name__ == "__main__":
    typer.run(main)
