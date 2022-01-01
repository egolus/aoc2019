from aocd import submit, get_data
from pprint import pprint


def main():
    day = 3
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        """R8,U5,L5,D3
U7,R6,D4,L4""": 6,
        """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""": 159,
        """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""": 135,
    }
    test_data_b = {
        """R8,U5,L5,D3
U7,R6,D4,L4""": 30,
        """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""": 610,
        """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""": 410,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def solve_a(data):
    lines = {0: set(), 1: set()}
    data = data.splitlines()
    for i in range(2):
        x, y = 0, 0
        for mv in data[i].split(","):
            direction = mv[0]
            count = int(mv[1:])
            if direction == "U":
                for _ in range(count):
                    y += 1
                    lines[i].add((x, y))
            if direction == "D":
                for _ in range(count):
                    y -= 1
                    lines[i].add((x, y))
            if direction == "R":
                for _ in range(count):
                    x += 1
                    lines[i].add((x, y))
            if direction == "L":
                for _ in range(count):
                    x -= 1
                    lines[i].add((x, y))
    return min((abs(p[0]) + abs(p[1])) for p in lines[0] if p in lines[1])


def solve_b(data):
    slines = {0: set(), 1: set()}
    lines = {0: list(), 1: list()}
    data = data.splitlines()
    for i in range(2):
        x, y = 0, 0
        for mv in data[i].split(","):
            direction = mv[0]
            count = int(mv[1:])
            if direction == "U":
                for _ in range(count):
                    y += 1
                    slines[i].add((x, y))
                    lines[i].append((x, y))
            if direction == "D":
                for _ in range(count):
                    y -= 1
                    slines[i].add((x, y))
                    lines[i].append((x, y))
            if direction == "R":
                for _ in range(count):
                    x += 1
                    slines[i].add((x, y))
                    lines[i].append((x, y))
            if direction == "L":
                for _ in range(count):
                    x -= 1
                    slines[i].add((x, y))
                    lines[i].append((x, y))
    crosses = [p for p in slines[0] if p in slines[1]]
    return min([lines[0].index(c) + 1 + lines[1].index(c) + 1 for c in crosses])


if __name__ == "__main__":
    main()
