import re
from dataclasses import dataclass, field

from functional import seq

from solver import Solver


class SolverImpl(Solver):
    _BUTTON_REGEX = re.compile(r"\s*Button (?P<name>\w+): X\+(?P<x>-?\d+), Y\+?(?P<y>-?\d+)")
    _PRIZE_REGEX = re.compile(r"\s*Prize: X=(?P<x>\d+), Y=(?P<y>\d+)")

    @dataclass
    class Game:
        buttons: dict[str, tuple[int, int]] = field(default_factory=dict)
        prize: tuple[int, int] | None = None

    def solve_part_1(self, data: str) -> int:
        games = [self.Game()]
        index = 0
        button_match, prize_match = self._BUTTON_REGEX.match(data, pos=index), self._PRIZE_REGEX.match(data, pos=index)
        while any((button_match, prize_match, )):
            if button_match and (
                    (not prize_match) or
                    (button_match.end() < prize_match.start())
            ):
                games[-1].buttons[button_match.group("name")] = int(button_match.group("x")), int(button_match.group("y"))
                index = button_match.span()[1] + 1
            elif prize_match and (
                    (not button_match) or
                    (prize_match.end() < button_match.start())
            ):
                games[-1].prize = int(prize_match.group("x")), int(prize_match.group("y"))
                games.append(self.Game())
                index = prize_match.span()[1] + 1
            else:
                raise ValueError("Unreachable code reached")
            button_match, prize_match = self._BUTTON_REGEX.match(data, pos=index), self._PRIZE_REGEX.match(data, pos=index)
        if games[-1].prize is None:
            games.pop()

        return seq(games).map(self._solve_game).sum()

    def _solve_game(self, game: Game) -> int:
        # A * ax + B * bx - px = A * ay + B * by - py
        # A = px - py
        px, py = game.prize
        ax, ay = game.buttons["A"]
        bx, by = game.buttons["B"]
        A = (
            ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
        )
        B = (py - (A * ay)) / by
        if A.is_integer() and B.is_integer():
            return int(3 * A + B)
        else:
            return 0

    def solve_part_2(self, data: str) -> int:
        games = [self.Game()]
        index = 0
        button_match, prize_match = self._BUTTON_REGEX.match(data, pos=index), self._PRIZE_REGEX.match(data, pos=index)
        while any((button_match, prize_match, )):
            if button_match and (
                    (not prize_match) or
                    (button_match.end() < prize_match.start())
            ):
                games[-1].buttons[button_match.group("name")] = int(button_match.group("x")), int(button_match.group("y"))
                index = button_match.span()[1] + 1
            elif prize_match and (
                    (not button_match) or
                    (prize_match.end() < button_match.start())
            ):
                games[-1].prize = 10000000000000 + int(prize_match.group("x")), 10000000000000 + int(prize_match.group("y"))
                games.append(self.Game())
                index = prize_match.span()[1] + 1
            else:
                raise ValueError("Unreachable code reached")
            button_match, prize_match = self._BUTTON_REGEX.match(data, pos=index), self._PRIZE_REGEX.match(data, pos=index)
        if games[-1].prize is None:
            games.pop()

        return seq(games).map(self._solve_game).sum()
