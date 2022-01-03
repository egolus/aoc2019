from itertools import count
from math import gcd
from functools import reduce
from aocd import submit, get_data
from pprint import pprint


def main():
    day = 12
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        ("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""", 10): 179,
        ("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""", 100): 1940,
    }
    test_data_b = {
        """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""": 2772,
        """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""": 4686774924,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data, 1000)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def printStep(moons, step):
    print()
    print("after step", step)
    for moon in moons:
        print(f"pos=<x={moon['gravity']['x']:>3}, y={moon['gravity']['y']:>3}, z={moon['gravity']['z']:>3}>, vel=<x={moon['velocity']['x']:>3}, y={moon['velocity']['y']:>3}, z={moon['velocity']['z']:>3}>")
    if "potential" in moons[0]:
        for moon in moons:
            print(f"pot: {moon['potential']}, kin: {moon['kinetic']}, total: {moon['total']}")
        print("sum of total energy:", sum(m['total'] for m in moons))


def solve_a(data, steps):
    moons = []
    for moon in data.splitlines():
        gravity = {}
        for axis in moon[1:-1].split(", "):
            split = axis.split("=")
            gravity[split[0]] = int(split[1])

        moons.append({
            "velocity": {"x": 0, "y": 0, "z": 0},
            "gravity": gravity,
        })
    printStep(moons, 0)
    print()

    for step in range(1, steps + 1):
        newMoons = []
        for moon in moons:
            newVel = dict(moon["velocity"].items())
            newGrv = dict(moon["gravity"].items())
            for other in moons:
                if other == moon:
                    continue
                for axis in ("x", "y", "z"):
                    if moon["gravity"][axis] > other["gravity"][axis]:
                        newVel[axis] -= 1
                    elif moon["gravity"][axis] < other["gravity"][axis]:
                        newVel[axis] += 1
            for axis in ("x", "y", "z"):
                newGrv[axis] += newVel[axis]
            pot = sum(abs(v) for v in newGrv.values())
            kin = sum(abs(v) for v in newVel.values())
            tot = pot * kin
            newMoons.append({"velocity": newVel, "gravity": newGrv, "potential": pot, "kinetic": kin, "total": tot})
        moons = newMoons

        if (not step % 10) or step < 11:
            printStep(moons, step + 1)
            print()
    return sum(m['total'] for m in moons)


def solve_b(data):
    steps = []
    moons = []
    periods = {}
    for moon in data.splitlines():
        gravity = {}
        for axis in moon[1:-1].split(", "):
            split = axis.split("=")
            gravity[split[0]] = int(split[1])

        moons.append((gravity["x"], gravity["y"], gravity["z"], 0, 0, 0))
    steps.append(moons)
    print("initial")
    for moon in moons:
        print(moon)
    print()

    k = 5
    for step in count(1):
        newMoons = []
        for j, moon in enumerate(moons):
            newGrv = list(moon[:3])
            newVel = list(moon[3:])
            for other in moons:
                if other == moon:
                    continue
                for i in range(3):
                    if moon[i] > other[i]:
                        newVel[i] -= 1
                    elif moon[i] < other[i]:
                        newVel[i] += 1
            for i in range(3):
                newGrv[i] += newVel[i]
            newMoons.append((*newGrv, *newVel))
            if newVel == [0, 0, 0]:
                print("no vel:", j, step)
            if j not in periods:
                for s in steps:
                    if s[j] == (*newGrv, *newVel):
                        print("found cycle for", j, "-", step)
                        periods[j] = step
        moons = newMoons
        if newMoons in steps:
            print(newMoons)
            return step
        steps.append(newMoons)
        # if len(periods) == len(moons):
            # k -= 1
            # if k == 0:
                # break
    print(periods)
    for j in range(len(moons)):
        print(j, periods[j], steps[periods[j] - 1][j], steps[periods[j]][j], steps[periods[j] + 1][j])
    res = reduce((lambda x, y: x*y//gcd(x, y)), periods.values())
    return res


if __name__ == "__main__":
    main()
