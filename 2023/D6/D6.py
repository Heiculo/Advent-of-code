# AOC 2023 Day 6
# Eetu Heikurinen

# PT 1
def times(File):
    Time = []
    Times = File.readline().strip()
    Times = Times.split(":")[1]
    i = 0
    while i < len(Times):
        if Times[i].isdigit() and Times[i+1].isdigit():
            Time.append(Times[i]+Times[i+1])
            i += 2
        elif Times[i] == " ":
            i += 1
    
    return Time

def lengths(File):
    Length = []
    Lengths = File.readline().strip()
    Lengths = Lengths.split(":")[1]
    i = 0
    while i < len(Lengths):
        if Lengths[i].isdigit() and Lengths[i+1].isdigit():
            Length.append(Lengths[i]+Lengths[i+1])
            i += 2
        elif Lengths[i] == " ":
            i += 1
    return Length

def distance(Time, Length):
    x = 0
    Record = []
    while x <len(Time):
        for i in range(0,Time[x]):
            if i*Time[x]-i > Length[x]:
                Record.append[i]
                i += 1
            else: i += 1
        x += 1
    print(Record)
    return Record

def main():
    File = open("D6.txt","r")
    Time = times(File)
    print(Time)
    Length = lengths(File)
    print(Length)
    Record = distance(Time, Length)
    return None

main()


