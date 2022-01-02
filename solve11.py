from collections import defaultdict
from aocd import submit, get_data
from computer import Computer


def main():
    day = 11
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
    }
    test_data_b = {
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
    cmp = Computer((int(d) for d in data.split(",")))
    hull = defaultdict(int)
    position = (0, 0)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    while not cmp.halted:
        color = cmp.run((hull[position],))
        dirChange = cmp.run(())
        if not cmp.halted:
            hull[position] = color
            direction = (direction + (1 if dirChange else -1)) % len(directions)
            position = (position[0] + directions[direction][0],
                        position[1] + directions[direction][1])
            print(hull[position], directions[direction], position)
    print(len(hull))
    return len(hull)


def solve_b(data):
    cmp = Computer((int(d) for d in data.split(",")))
    hull = defaultdict(int)
    hull[(0, 0)] = 1
    position = (0, 0)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    while not cmp.halted:
        color = cmp.run((hull[position],))
        dirChange = cmp.run(())
        if not cmp.halted:
            hull[position] = color
            direction = (direction + (1 if dirChange else -1)) % len(directions)
            position = (position[0] + directions[direction][0],
                        position[1] + directions[direction][1])
            print(hull[position], directions[direction], position)
    maxX = max(hull, key=lambda x: x[0])[0]
    minX = min(hull, key=lambda x: x[0])[0]
    maxY = max(hull, key=lambda x: x[1])[1]
    minY = min(hull, key=lambda x: x[1])[1]
    for y in range(minY, maxY + 1):
        print("".join("#" if hull[x, y] else "." for x in range(minX, maxX + 1)))


if __name__ == "__main__":
    main()
