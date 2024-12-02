from solver import Solver


class SolverImpl(Solver):

    def solver_part_1(self, data: str) -> int:
        safe = 0
        for line in data.strip().splitlines():
            parts = line.split()
            if self._is_report_safe(parts):
                safe += 1
        return safe

    def _is_report_safe(self, parts):
        last = None
        this_line_is_safe = True
        increasing = None
        for part in parts:
            part = int(part)
            if last is None:
                pass
            elif not (1 <= abs(last - part) <= 3):
                this_line_is_safe = False
                break
            elif increasing is None:
                increasing = part > last
            elif increasing and part < last:
                this_line_is_safe = False
                break
            elif not increasing and part > last:
                this_line_is_safe = False
                break
            elif part == last:
                this_line_is_safe = False
                break
            last = part
        return this_line_is_safe

    def solve_part_2(self, data: str) -> int:
        safe = 0
        for line in data.strip().splitlines():
            parts = line.split()
            if self._is_report_safe(parts):
                safe += 1
            else:
                for i in range(len(parts)):
                    lhs = parts[:i] if i > 0 else []
                    rhs = parts[i + 1:] if i < len(parts) - 1 else []
                    new_report = lhs + rhs
                    if self._is_report_safe(new_report):
                        safe += 1
                        break
        return safe
