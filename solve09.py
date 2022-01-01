from aocd import submit, get_data
from computer import Computer


def main():
    day = 9
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99":
        [int(x) for x in "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(",")]
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
    cmp = Computer([int(d) for d in data.split(",")])
    outputs = []
    while not cmp.halted:
        o = cmp.run((1, ))
        if o is not None:
            outputs.append(o)
    print(outputs)
    if len(outputs) == 1:
        return outputs[0]
    return outputs


def solve_b(data):
    cmp = Computer([int(d) for d in data.split(",")])
    outputs = []
    while not cmp.halted:
        o = cmp.run((2, ))
        if o is not None:
            outputs.append(o)
    print(outputs)
    if len(outputs) == 1:
        return outputs[0]
    return outputs


if __name__ == "__main__":
    main()
