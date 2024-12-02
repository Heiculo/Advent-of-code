# Eetu Heikurinen
# 2.12.2024, AoC 2021 Day 2

def main_P1():
    data = open("AoC\\2021\\D2_2021.txt", "r")
    horizontal = 0
    depth = 0

    
    
    for row in data:
        dir, num = row.split()
        if "forward" in row:
            horizontal += int(num)
        elif "down" in row:
            depth += int(num)
        elif "up" in row:
            depth -= int(num)
    final = horizontal*depth
    print(f"Part 1: {final}")
    return

def main_P2():
    data = open("AoC\\2021\\D2_2021.txt", "r")
    horizontal = 0
    depth = 0
    aim = 0


    for row in data:
        dir, num = row.split()
        if "forward" in row:
            horizontal += int(num)
            depth += int(num)*aim
        elif "down" in row:
            aim += int(num)
        elif "up" in row:
            aim -= int(num)
    final = horizontal*depth
    print(f"Part 2: {final}")
    return

main_P1()
main_P2()