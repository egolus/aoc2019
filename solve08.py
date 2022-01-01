from aocd import submit, get_data
from sys import maxsize


def main():
    day = 8
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
    i = 0
    zeros = maxsize
    res = 0
    while i < len(data):
        print()
        layer = data[i:(i+25*6)]
        for j in range(6):
            print(layer[j*25:(j+1)*25])
        z = len(list(filter(lambda x: x == "0", layer)))
        o = len(list(filter(lambda x: x == "1", layer)))
        t = len(list(filter(lambda x: x == "2", layer)))
        print("z:", z)
        print("o:", o, "t:", t)
        if z < zeros:
            zeros = z
            res = o * t
        i += (25 * 6)
    return res


def solve_b(data):
    output = list(["2"] * 25 * 6)
    i = 0
    while i < len(data):
        layer = data[i:i+25*6]
        i += 25 * 6
        for j, c in enumerate(layer):
            if output[j] == "2":
                output[j] = c
    for i in range(6):
        for c in output[i*25:(i+1)*25]:
            if c == "0":
                print(".", end="")
            elif c == "1":
                print("#", end="")
            else:
                print("-", end="")
        print()


if __name__ == "__main__":
    main()
