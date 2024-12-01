# AOC 2023 Day 3
# Eetu Heikurinen

# P1
def main():
    File = open("D4.txt", "r")
    Row = File.readline()
    Final = []
    while len(Row)>0:
        Numbers = Row.split(":")[1]
        WinningNumbers, Values = Numbers.split("|")
        Winning = []
        W = []
        Testing = []
        T = []
        for Number in WinningNumbers:
            Winning.append(Number)
        i = 0
        while i < len(Winning):
            if Winning[i].isdigit() and Winning[i+1].isdigit():
                Combined = Winning[i]+Winning[i+1]
                i += 2
                W.append(Combined)
            elif Winning[i].isdigit() and Winning[i+1] == " ":
                W.append(Winning[i])
                i += 1
            else:
                i += 1

        for Number in Values:
            Testing.append(Number)
        i = 0
        while i < len(Testing)-1:
            if Testing[i].isdigit() and Testing[i+1].isdigit():
                Combined = Testing[i]+Testing[i+1]
                i += 2
                T.append(Combined)
            elif Testing[i].isdigit() and Testing[i+1] == " ":
                T.append(Testing[i])
                i += 1
            elif Testing[i].isdigit and Testing[i+1] == "\n":
                T.append(Testing[i])
                i += 1
            else:
                i += 1

        Sum = 0
        for Number in W:
            if Number in T:
                Sum += 1
        if Sum != 0:
            Value = 2**(Sum-1)
            Final.append(Value)
            Row = File.readline()
        else:
            Row = File.readline()

    Sum = 0
    print(Final)
    for Value in Final:
        Sum += Value
    print(Sum)

    return None


main()

# P2
