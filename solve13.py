from collections import defaultdict
from aocd import submit, get_data
from computer import Computer
from time import sleep


def main():
    day = 13
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


class Game:
    cmp = None
    screen = None
    score = 0
    debug = False
    posBall: tuple = (0, 0)
    posPaddle: tuple = (0, 0)
    move = None

    def __init__(self, data, debug=False):
        self.debug = debug
        self.cmp = Computer([int(x) for x in data.split(",")], debug=debug)
        self.screen = defaultdict(int)
        inst = []
        while not self.cmp.halted:
            ret = self.cmp.run((self.move,))
            self.move = None
            if ret is not None:
                inst.append(ret)
                if len(inst) >= 3:
                    if inst[0] == -1:
                        self.score = inst[2]
                    else:
                        self.screen[(inst[0], inst[1])] = inst[2]
                        if inst[2] == 3:
                            self.posPaddle = (inst[0], inst[1])
                        elif inst[2] == 4:
                            self.posBall = (inst[0], inst[1])
                    inst = []
            if self.cmp.waitingForInput:
                self.printScreen()
                self.move = 0
                if self.posBall[0] < self.posPaddle[0]:
                    self.move = -1
                elif self.posBall[0] > self.posPaddle[0]:
                    self.move = 1

    def printScreen(self):
        maxX = max(inst[0] for inst in self.screen)
        maxY = max(inst[1] for inst in self.screen)
        print("score:", self.score)
        print("posPaddle:", self.posPaddle)
        print("posBall:", self.posBall)
        print()
        for y in range(maxY + 1):
            for x in range(maxX + 1):
                pixel = self.screen[(x, y)]
                if pixel == 0:
                    # empty
                    print(".", end="")
                elif pixel == 1:
                    # wall
                    print("#", end="")
                elif pixel == 2:
                    # block
                    print("x", end="")
                elif pixel == 3:
                    # horizontal paddle
                    print("=", end="")
                elif pixel == 4:
                    # ball
                    print("o", end="")
                else:
                    print(" ", end="")
            print()
        sleep(0.1)


def solve_a(data):
    game = Game(data)
    return len([x for x in game.screen.values() if x == 2])


def solve_b(data):
    data = "2" + data[1:]
    game = Game(data)
    return game.score


if __name__ == "__main__":
    main()
