from time import sleep
from aocd import submit, get_data
from computer import Computer


def main():
    day = 15
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


class Map:
    cmp: Computer = None
    space = {}
    position = (0, 0)
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    dirCode = (1, 4, 2, 3)
    direction = 0
    toSearch = 0

    # directions:
    # 1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)

    # return values / space values
    # 0: wall
    # 1: moved
    # 2: found
    # -1: (not explored, yet)
    # 3: exhausted

    def __init__(self, data):
        self.cmp = Computer(int(d) for d in data.split(","))
        self.space[self.position] = 6 + self.direction

    def solve(self):
        k = 0
        while not self.cmp.halted:
            if not self.cmp.waitingForInput:
                print("running without input")
                self.cmp.run()
                continue
            for pos in (
                (self.position[0] - 1, self.position[1]),
                (self.position[0] + 1, self.position[1]),
                (self.position[0], self.position[1] - 1),
                (self.position[0], self.position[1] + 1),
            ):
                if pos not in self.space:
                    self.space[pos] = -1
                    self.toSearch += 1
            if self.toSearch == 0:
                self.printSpace()
                print(self.position)
                for y in range(self.position[1] - 2, self.position[1] + 3):
                    for x in range(self.position[0] - 2, self.position[0] + 3):
                        try:
                            print(f"position[({x}, {y})]: {self.space[(x, y)]}")
                        except:
                            pass
                break
            self.printSpace()
            # for i in (range(5) if k < 250 else range(-1, 4)):
            # for i in (range(-1, 4) if k else range(1, -4, -1)):
            for i in range(4):
                # direction = (self.direction + i) % 4
                direction = i
                test = (self.position[0] + self.directions[direction][0],
                        self.position[1] + self.directions[direction][1])
                if self.space[test] == -1:
                    self.toSearch -= 1
                    self.direction = direction
                    ret = self.cmp.run((self.dirCode[self.direction],))
                    print("ret", repr(ret))
                    print("k", k)
                    print("toSearch", self.toSearch)
                    if ret == 2:
                        return test
                    self.space[test] = ret
                    if ret == 1:
                        self.position = test
                        self.space[self.position] = 6 + self.direction
                    break
            else:
                k = (k + 1) % 2
                direction = self.space[self.position] % 4
                test = (self.position[0] + self.directions[direction][0],
                        self.position[1] + self.directions[direction][1])
                ret = self.cmp.run((1,))
                print("ret", ret)
                print("k", k)
                print("toSearch", self.toSearch)
                self.position = test
            # if not k % 10:
                # input()

    def printSpace(self):
        minX = min(x[0] for x in self.space)
        maxX = max(x[0] for x in self.space)
        minY = min(x[1] for x in self.space)
        maxY = max(x[1] for x in self.space)
        for y in range(minY -1, maxY + 1):
            for x in range(minX -1, maxX + 1):
                pixel = self.space.get((x, y),-2)
                try:
                    if self.position == (x, y):
                        print("x", end="")
                    elif (x, y) == (0, 0):
                        print("s", end= "")
                    elif pixel == -1:
                        print("o", end="")
                    elif pixel == 0:
                        print("#", end="")
                    elif pixel == 1:
                        print(".", end="")
                    elif pixel == 2:
                        print("t", end="")
                    # elif pixel > 2:
                        # print(pixel, end="")
                    else:
                        print(" ", end="")
                except:
                    print(pixel)
                    raise
            print()
        print()
        # sleep(0.05)


def solve_a(data):
    target = Map(data).solve()
    print(target)


def solve_b(data):
    ...


if __name__ == "__main__":
    main()
