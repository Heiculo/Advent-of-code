# Eetu Heikurinen
# 10.10.2024
# P1

def main_P1():
    file = open("AoC\\2015\\D1\\D1_2015.txt","r")
    row = file.readline()
    floor = 0
    for char in row:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    
    return floor

print(f"Part 1: {main_P1()}")

# P2

def main_P2():
    file = open("AoC\\2015\\D1\\D1_2015.txt","r")
    row = file.readline()
    floor = 0
    char_num = 0
    for char in row:  
        char_num += 1
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return char_num
        
        
    return char_num

print(f"Part 2: {main_P2()}")