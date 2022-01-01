from aocd import submit, get_data


def main():
    day = 4
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
    }
    test_data_b = {
    }

    check_data = {
        "111111": True,
        "223450": False,
        "123789": False,
    }

    check_data_b = {
        "112233": True,
        "123444": False,
        "111122": True,
    }

    for i, (test, true) in enumerate(check_data.items()):
        result = check(test)
        print(f"check result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(check_data_b.items()):
        result = check_b(test)
        print(f"check result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def check(pw):
    double = False
    for i in range(1, len(pw)):
        if pw[i] < pw[i-1]:
            return False
        if pw[i] == pw[i-1]:
            double = True
    return double


def solve_a(data):
    from_, to_ = data.split("-")
    return sum(check(str(i)) for i in range(int(from_), int(to_) + 1))


def check_b(pw):
    double = False
    for i in range(1, len(pw)):
        if pw[i] < pw[i-1]:
            return False
        if ((pw[i] == pw[i-1])
                and (i == 1 or (pw[i] != pw[i-2]))
                and (i == (len(pw) - 1) or (pw[i] != pw[i+1]))):
            double = True
    return double



def solve_b(data):
    from_, to_ = data.split("-")
    return sum(check_b(str(i)) for i in range(int(from_), int(to_) + 1))


if __name__ == "__main__":
    main()
