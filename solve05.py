from aocd import submit, get_data
from computer import Computer


def main():
    day = 5
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
    }
    test_data_b = {
    }
    test_computer = {
        (1101,100,-1,4,0): 1101,
    }

    # for i, (test, true) in enumerate(test_computer.items()):
        # result = Computer(list(test)).run(None)
        # print(f"result {i}: {result}\n")
        # assert result == true, f"{result} != {true}"

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
    comp = Computer([int(inst) for inst in data.split(",")])
    return comp.run((1,))


def solve_b(data):
    comp = Computer([int(inst) for inst in data.split(",")])
    return comp.run((5,))


if __name__ == "__main__":
    main()
