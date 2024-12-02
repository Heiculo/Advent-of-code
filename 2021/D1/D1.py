# Eetu Heikurinen
# 2.12.2024, AoC 2022 Day 1

def main_P1():
    data = open("AoC\\2021\\D1\\D1_2021.txt","r")
    values = []
    for num in data:
        values.append(int(num))
    
    increase = 0
    i = 0
    while i < len(values)-1:
        if values[i+1]>values[i]:
            increase += 1
            i += 1
        else:
            i+= 1
    print(f"Increased: {increase}")
    return

def main_P2():
    data = open("AoC\\2021\\D1\\D1_2021.txt","r")
    values = []
    increase = 0
    for num in data:
        values.append(int(num))
    
    class_list = []
    i = 0
    while i<len(values)-2:
        class_list.append(values[i]+values[i+1]+values[i+2])
        i += 1
    i = 0
    while i < len(class_list)-1:
        if class_list[i+1]>class_list[i]:
            increase += 1
            i += 1
        else:
            i+= 1
    print(f"Classes increased: {increase}")
    return
    


main_P1()
main_P2()