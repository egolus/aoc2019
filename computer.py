class Computer:
    program: list = None
    instPointer: int = 0
    output: int = None
    halted = False

    def __init__(self, program):
        self.program = program

    def run(self, inputs):
        ipos = 0
        print("inputs:", inputs)
        while True:
            inst = str(self.program[self.instPointer]).rjust(5, "0")
            print("inst", self.instPointer, "->", inst)
            if inst[-2:] == "01":
                # add
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                o = self.program[self.instPointer+3]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    print(f"{inst}, {i0}, {i1}, {o}")
                self.program[o] = i0 + i1
                print("->", o, self.program[o])
                self.instPointer += 4
            elif inst[-2:] == "02":
                # mul
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                o = self.program[self.instPointer+3]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    print(f"{inst}, {i0}, {i1}, {o}")
                self.program[o] = i0 * i1
                print("->", o, self.program[o])
                self.instPointer += 4
            elif inst[-2:] == "03":
                # input
                if ipos >= len(inputs) or inputs[ipos] is None:
                    # wait for input
                    print("waiting for input")
                    return
                o = self.program[self.instPointer+1]
                self.program[o] = inputs[ipos]
                ipos += 1
                print(inst, o)
                print("->", o, self.program[o])
                self.instPointer += 2
            elif inst[-2:] == "04":
                # output
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                if self.program[self.instPointer+2] == 99:
                    print("HALT")
                    self.halted = True
                    # raise ComputerHalt(i0)
                self.instPointer += 2
                return i0
                # self.output = self.program[i0]
                # self.output = i0
                # print(inst, i0)
                # print(self.program[i0])
            elif inst[-2:] == "05":
                # jump-if-true
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                except:
                    print(f"{inst}, {i0}, {i1}")
                print("pointer before:", self.instPointer)
                if i0:
                    self.instPointer = i1
                else:
                    self.instPointer += 3
                print("pointer:", self.instPointer)
            elif inst[-2:] == "06":
                # jump-if-false
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}")
                except:
                    print(f"{inst}, {i0}, {i1}")
                if i0 == 0:
                    self.instPointer = i1
                else:
                    self.instPointer += 3
            elif inst[-2:] == "07":
                # less than
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                o = self.program[self.instPointer+3]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    print(f"{inst}, {i0}, {i1}, {o}")
                self.program[o] = 1 if i0 < i1 else 0
                print("->", o, self.program[o])
                self.instPointer += 4
            elif inst[-2:] == "08":
                # equals
                i0 = self.program[self.instPointer+1]
                if inst[-3] == "0":
                    i0 = self.program[i0]
                i1 = self.program[self.instPointer+2]
                if inst[-4] == "0":
                    i1 = self.program[i1]
                o = self.program[self.instPointer+3]
                try:
                    print(f"{inst}, {self.program[self.program[self.instPointer+1]]}/{self.program[self.instPointer+1]}, {self.program[self.program[self.instPointer+2]]}/{self.program[self.instPointer+2]}, {o}")
                except:
                    print(f"{inst}, {i0}, {i1}, {o}")
                self.program[o] = 1 if i0 == i1 else 0
                print("->", o, self.program[o])
                self.instPointer += 4
            elif inst[-2:] == "99":
                self.halted = True
                return
            else:
                print("illegal optcode")
                print(self.instPointer, inst, inst[3:5])
                self.printProgram()
                break
        # raise ComputerHalt(self.program[0])
        return self.program[0] if not self.output else self.output

    def printProgram(self):
        print("   ", end="")
        for self.instPointer in range(10):
            print(f"{self.instPointer:>8}", end="")
        print()
        print("  1", end="")
        for self.instPointer, val in enumerate(self.program):
            print(f"{val:>8}", end="")
            if not (self.instPointer + 1) % 10:
                print()
                print(f"{self.instPointer//10:>3}", end="")
