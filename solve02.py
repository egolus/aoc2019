from aocd import submit, get_data


def main():
    day = 2
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        "1,9,10,3,2,3,11,0,99,30,40,50": 3500,
        "1,0,0,0,99": 2,
        "2,3,0,3,99": 2,
        "1,1,1,4,99,5,6,0,99": 30,
    }
    test_data_b = {
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data, (12, 2))
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def solve_a(data, inputs=None):
    program = [int(x) for x in data.split(",")]
    if inputs:
        program[1] = inputs[0]
        program[2] = inputs[1]
    i = 0
    while True:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            i += 4
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            i += 4
        elif program[i] == 99:
            break
        else:
            print("illegal optcode")
            break
    return program[0]


def solve_b(data):
    searchvalue = 19690720
    for i in range(99):
        for j in range(99):
            res = solve_a(data, (i, j))
            if res == searchvalue:
                return 100 * i + j


if __name__ == "__main__":
    main()
