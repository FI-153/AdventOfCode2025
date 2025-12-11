from collections import deque
from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def parse_line(line: str) -> tuple[list[str], list[tuple[int, ...]], list[int]]:
    state_part, rest = line.split('] ')
    buttons_part, voltage_part = rest.split(' {')

    initial_state = ["0" if c == '.' else "1" for c in state_part[1:]]
    voltage = [int(x) for x in voltage_part[:-1].split(',')]
    buttons = [
        tuple(int(x) for x in b[1:-1].split(','))
        for b in buttons_part.split()
    ]

    return initial_state, buttons, voltage


def solve_line_part1(line: str) -> int:
    initial_state, buttons, _ = parse_line(line)
    start = int("".join(initial_state[::-1]), 2)
    button_masks = [sum(1 << idx for idx in button) for button in buttons]

    seen = set()
    queue = deque([(start, 0)])
    while queue:
        state, steps = queue.popleft()
        if state == 0:
            return steps
        if state in seen:
            continue
        seen.add(state)
        for mask in button_masks:
            queue.append((state ^ mask, steps + 1))

    raise ValueError(f"No solution found: {line}")


def solve_part1(data: str) -> int:
    return sum(solve_line_part1(line) for line in data.splitlines())


def solve_line_part2(line: str) -> int:
    """Solve Ax = b where x >= 0 integers, minimizing sum(x)."""
    _, buttons, voltage = parse_line(line)
    n_buttons = len(buttons)
    n_outputs = len(voltage)

    # Build matrix A: A[j][i] = 1 if button i affects output j
    A = np.zeros((n_outputs, n_buttons))
    for i, button in enumerate(buttons):
        for idx in button:
            if idx < n_outputs:
                A[idx, i] = 1

    b = np.array(voltage)

    # Minimize sum(x) subject to Ax = b, x >= 0, x integer
    c = np.ones(n_buttons)  # minimize sum of x
    constraints = LinearConstraint(A, b, b)  # Ax = b
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)

    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

    if not result.success:
        raise ValueError(f"No solution found: {line}")

    return int(round(result.fun))


def solve_part2(data: str) -> int:
    return sum(solve_line_part2(line) for line in data.splitlines())


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Min presses: {solve_part2(input_data)}")