from collections import defaultdict

class Computer:
    program: defaultdict = None
    instPointer: int = 0
    output: int = None
    halted = False
    relativeBase = 0
    debug = False

    def __init__(self, program, debug=False):
        self.debug = debug
        self.program = defaultdict(int)
        for i, c in enumerate(program):
            self.program[i] = c

    def run(self, inputs):
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    if self.debug:
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    if self.debug:
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                except:
                    if self.debug:
                        print(f"{inst}, {i0}, {i1}")
                if self.debug:
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                except:
                    if self.debug:
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    if self.debug:
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
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    if self.debug:
                        print(f"{inst}, {i0}, {i1}, {o}")
                self.write(o, inst[-5], 1 if i0 == i1 else 0)
                self.instPointer += 4
            elif inst[-2:] == "09":
                # adjust relative base
                if self.debug:
                    print("adjust relative base")
                i0 = self.loadVal(self.instPointer+1, inst[-3])
                try:
                    if self.debug:
                        print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}")
                except:
                    if self.debug:
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
                if self.debug:
                    print("illegal optcode")
                    print(self.instPointer, inst, inst[3:5])
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
