from collections import defaultdict


class Computer:
    program: defaultdict = None
    instPointer: int = 0
    output: int = None
    halted = False
    waitingForInput = False
    relativeBase = 0
    debug = False

    def __init__(self, program, debug=False):
        self.debug = debug
        self.program = defaultdict(int)
        for i, c in enumerate(program):
            self.program[i] = c

    # instructions:
    # 1 - add - 2 input 1 output
    # 2 - mul - 2 input 1 output
    # 3 - input - 1 output
    # 4 - output - 1 input
    # 5 - jump-if-true - 2 input
    # 6 - jump-if-false - 2 input
    # 7 - less than - 2 input 1 output
    # 8 - equals - 2 input 1 output
    # 9 - adjust relative base - 1 input
    # 99 - halt
    def run(self, inputs=None):
        if inputs is None:
            inputs = []
        self.waitingForInput = False
        ipos = 0
        if self.debug:
            print("inputs:", inputs)
        while True:
            inst = str(self.program[self.instPointer]).rjust(5, "0")
            if self.debug:
                print("inst", self.instPointer, "->", inst, ": ", end="")
            if inst[-2:] == "01":
                # add
                if self.debug:
                    print("add")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                o = self.program[self.instPointer+3]
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                    except:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.write(o, inst[-5], i0 + i1)
                self.instPointer += 4
            elif inst[-2:] == "02":
                # mul
                if self.debug:
                    print("mul")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                o = self.program[self.instPointer+3]
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                    except:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.write(o, inst[-5], i0 * i1)
                self.instPointer += 4
            elif inst[-2:] == "03":
                # input
                if self.debug:
                    print("input")
                if ipos >= len(inputs) or inputs[ipos] is None:
                    # wait for input
                    if self.debug:
                        print("waiting for input")
                    self.waitingForInput = True
                    return
                o = self.program[self.instPointer+1]
                self.write(o, inst[-3], inputs[ipos])
                ipos += 1
                self.instPointer += 2
            elif inst[-2:] == "04":
                # output
                if self.debug:
                    print("output")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                if self.program[self.instPointer+2] == 99:
                    if self.debug:
                        print("HALT")
                    self.halted = True
                self.instPointer += 2
                return i0
            elif inst[-2:] == "05":
                # jump-if-true
                if self.debug:
                    print("jump-if-true")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                    except:
                        print(f"{inst}, {i0}, {i1}")
                    print("pointer before:", self.instPointer)
                if i0:
                    self.instPointer = i1
                else:
                    self.instPointer += 3
                if self.debug:
                    print("pointer:", self.instPointer)
            elif inst[-2:] == "06":
                # jump-if-false
                if self.debug:
                    print("jump-if-false")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                    except:
                        print(f"{inst}, {i0}, {i1}")
                if i0 == 0:
                    self.instPointer = i1
                else:
                    self.instPointer += 3
                if self.debug:
                    print("pointer:", self.instPointer)
            elif inst[-2:] == "07":
                # less than
                if self.debug:
                    print("less than")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                o = self.program[self.instPointer+3]
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                    except:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.write(o, inst[-5], 1 if i0 < i1 else 0)
                self.instPointer += 4
            elif inst[-2:] == "08":
                # equals
                if self.debug:
                    print("equals")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                i1 = self.loadVal(self.instPointer+2, inst[-4])
                o = self.program[self.instPointer+3]
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                    except:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.write(o, inst[-5], 1 if i0 == i1 else 0)
                self.instPointer += 4
            elif inst[-2:] == "09":
                # adjust relative base
                if self.debug:
                    print("adjust relative base")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                if self.debug:
                    try:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}")
                    except:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.relativeBase += i0
                if self.debug:
                    print("relative base:", self.relativeBase)
                self.instPointer += 2
            elif inst[-2:] == "99":
                if self.debug:
                    print("stop/halt")
                self.halted = True
                return
            else:
                print("illegal optcode")
                print(self.instPointer, inst, inst[3:5])
                if self.debug:
                    self.printProgram()
                self.halted = True
                break
        return self.program[0] if not self.output else self.output

    def loadVal(self, address, mode):
        if self.debug:
            print(f"loadval - a: {address}, m: {mode}")
        val = self.program[address]
        if self.debug:
            print(f"direct: {val}")
        if mode == "0":
            val = self.program[val]
            if self.debug:
                print(f"after {mode}: {val}")
        elif mode == "2":
            val = self.program[self.relativeBase + val]
            if self.debug:
                print(f"after {mode}: {val} (base: {self.relativeBase})")
        return val

    def write(self, o, mode, val):
        if self.debug:
            print(f"write - o: {o}, m: {mode}, v: {val}")
        if mode == "2":
            self.program[self.relativeBase + o] = val
            if self.debug:
                print("->", self.relativeBase + o, self.program[self.relativeBase + o])
        else:
            self.program[o] = val
            if self.debug:
                print("->", o, self.program[o])

    def printProgram(self):
        for i, val in sorted(self.program.items()):
            print(f"{i:>10}: {val}")
