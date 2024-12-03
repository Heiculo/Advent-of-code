# Eetu Heikurinen
# 3.12.2024, AoC 2024 Day 3

import re

def main_P1():
    data = open("AoC\\2024\\D3\\D3_2024.txt","r")

    # form a single string from data
    data_string = "".join(data)

    # Find all the occurances of the wanted string format
    matches = re.findall(r"mul\((\d+),(\d+)\)",data_string)

    sum = 0
    for num in matches:
        sum += int(num[0])*int(num[1])

    print(f"Part 1: {sum}")

    return

def main_P2():
    data = open("AoC\\2024\\D3\\D3_2024.txt","r")

    # form a single string from data
    data_string = "".join(data)
    do = data_string.split("do()")

    # Find all the strings that follow do()
    do_list = []
    for item in do:
        try:
            # Split those strings by dont()'s and add the parts before the dont() into a new data list
            list = item.split("don't()")
            do_list.append(list[0])
        except: 
            do_list.append(item)
    print(do_list)
    dos_string = "".join(do_list)

    matches = re.findall(r"mul\((\d+),(\d+)\)",dos_string)

    sum = 0
    for num in matches:
        sum += int(num[0])*int(num[1])

    print(f"Part 2: {sum}")

    return

main_P1()
main_P2()


