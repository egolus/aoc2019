from aocd import submit, get_data


def main():
    day = 1
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        """12
14
1969
100756""": 2 + 2 + 654 + 33583,
    }
    test_data_b = {
        """14
1969
100756""": 2 + 966 + 50346
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
    for line in data.splitlines():
        res += int(line) // 3 - 2
    return res


def solve_b(data):
    fuel = 0
    for line in data.splitlines():
        linefuel = int(line) // 3 - 2
        print(f"base fuel for {line}: {linefuel}")
        new = linefuel
        while True:
            new = new // 3 - 2
            if new <= 0:
                break
            print(f"    added: {new}")
            linefuel += new
        print(f"fuel for {line}: {linefuel}")
        fuel += linefuel
    print(f"all fuel: {fuel}")
    return fuel


if __name__ == "__main__":
    main()
