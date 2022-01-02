from aocd import submit, get_data
from math import atan, pi, sqrt
from collections import defaultdict
from pprint import pprint


def main():
    day = 10
    year = 2019
    data = get_data(day=day, year=year)

    test_data_a = {
        """.#..#
.....
#####
....#
...##""": 8,
        """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""": 33,
        """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""": 35,
        """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""": 41,
        """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""": 210,
    }
    test_data_b = {
        (""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##""", (8, 3)): 1403,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result[1] == true, f"{result[1]} != {true}"

    result_a = solve_a(data)
    submit(result_a[1], part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data, result_a[0])
    submit(result_b, part="b", day=day, year=year)


def solve_a(data):
    asteroids = set()
    res = None
    maxsight = 0
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "#":
                asteroids.add((j, i))
    for a in asteroids:
        sight = set()
        for o in asteroids:
            if o == a:
                continue
            n = (o[0] - a[0], o[1] - a[1])
            if n[0] == 0:
                if n[1] > 0:
                    sight.add(pi / 2)
                else:
                    sight.add(3 * pi / 2)
            elif n[0] > 0:
                sight.add(atan(n[1] / n[0]))
            else:
                sight.add(atan(n[1] / n[0]) + pi)
        if len(sight) > maxsight:
            maxsight = len(sight)
            res = a
    print (res, maxsight)
    return (res, maxsight)


def solve_b(data, pos):
    res: tuple = None
    asteroids = set()
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "#":
                asteroids.add((j, i))
    sight = defaultdict(list)
    for o in asteroids:
        if o == pos:
            continue
        n = (o[0] - pos[0], (o[1] - pos[1]) * (-1))
        if n[0] == 0:
            if n[1] > 0:
                sight[(3 * pi) / 2].append(o)
            else:
                sight[pi / 2].append(o)
        elif n[0] > 0:
            sight[atan(n[1] / n[0])].append(o)
        else:
            sight[atan(n[1] / n[0]) - pi].append(o)

    for theta in sight:
        sight[theta] = sorted(sight[theta],
                              key=lambda x: sqrt((x[0]-pos[0])**2 +
                                                 (x[1]-pos[1])**2))
    i = 0
    last = None
    while True:
        for theta in sorted(sight, reverse=True):
            if not sight[theta]:
                continue
            i += 1
            last = sight[theta].pop(0)
            if i >= 200:
                break
        if i >= 200 or not sum(len(x) for x in sight.values()):
            break

    return last[0] * 100 + last[1]


if __name__ == "__main__":
    main()
