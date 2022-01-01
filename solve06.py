from aocd import submit, get_data


def main():
    day = 6
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""": 42,
    }
    test_data_b = {
        """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""": 4,
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
    res = 0
    orbits = {}
    for line in data.splitlines():
        par, chi = line.split(")")
        orbits[chi] = par
    for chi, parent in orbits.items():
        while parent:
            res += 1
            parent = orbits.get(parent, None)
    return res


def solve_b(data):
    res = 0
    orbits = {}
    for line in data.splitlines():
        par, chi = line.split(")")
        orbits[chi] = par
    sanchain = []
    parent = orbits["SAN"]
    while parent:
        sanchain.append(parent)
        parent = orbits.get(parent, None)
    parent = orbits["YOU"]
    while parent not in sanchain:
        res += 1
        parent = orbits.get(parent, None)
    res += sanchain.index(parent)
    return res


if __name__ == "__main__":
    main()
