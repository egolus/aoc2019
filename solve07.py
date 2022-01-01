from aocd import submit, get_data
from itertools import permutations
from computer import Computer, ComputerHalt
from pprint import pprint


def main():
    day = 7
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
    }
    test_data_b = {
        "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5": 139629729,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    # submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def solve_a(data):
    amplifiers = []
    for i in range(5):
        amplifiers.append({"phase": None, "input": None, "output": None})

    for perm in permutations(range(5)):
        amps = []
        for _ in range(5):
            amps.append({"phase": None, "input": None, "output": None})
        for i, amp in enumerate(amps):
            cmp = Computer([int(inst) for inst in data.split(",")])
            if i == 0:
                amp["input"] = 0
            amp["phase"] = perm[i]
            # try:
            amp["output"] = cmp.run((amp["phase"], amp["input"]))
            if not amp["output"]:
                amp["output"] = cmp.output
            if i < 4:
                amps[i+1]["input"] = amp["output"]
        try:
            if amplifiers[-1]["output"] is None or amps[-1]["output"] > amplifiers[-1]["output"]:
                amplifiers = amps
        except Exception:
            pprint(amps)
            pprint(amplifiers)
            continue
    return amplifiers[-1]["output"]


def solve_b(data):
    amplifiers = []
    for i in range(5):
        amplifiers.append(
            {
                "phase": None,
                "inputs": [],
                "outputs": [],
            })
    for perm in permutations(range(5, 10)):
        amps = []
        for i in range(5):
            amps.append(
                {
                    "phase": perm[i],
                    "inputs": [],
                    "outputs": [],
                    "cmp": Computer([int(inst) for inst in data.split(",")]),
                })
        for i, amp in enumerate(amps):
            print("-----------------")
            print(f"amp: {i} (phase)")
            amp["cmp"].run((amp["phase"], ))
        amps[0]["inputs"].append(0)
        while True:
            for i, amp in enumerate(amps):
                print("-----------------")
                print(f"amp: {i}")
                if amp["cmp"].halted:
                    print("computer has halted")
                    break
                try:
                    o = amp["cmp"].run((amp["inputs"][-1], ))
                    print("output:", o)
                    if not o:
                        if amp["cmp"].halted:
                            continue
                        o = amp["cmp"].output
                        print("cmp.output:", o)
                except Exception as e:
                    break
                if o is not None:
                    amp["outputs"].append(o)
                    amps[(i+1) % 5]["inputs"].append(amp["outputs"][-1])
            else:
                continue
            break
        try:
            if not amplifiers[-1]["outputs"] or amps[-1]["outputs"][-1] > amplifiers[-1]["outputs"][-1]:
                amplifiers = amps
        except Exception:
            print(amps)
            print(amplifiers)
            continue
    pprint(amplifiers)
    return amplifiers[-1]["outputs"][-1]


if __name__ == "__main__":
    main()
