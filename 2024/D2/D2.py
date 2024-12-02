# Eetu Heikurinen
# 2.12.2024, AoC 2024 Day 2

def main_P1():
    data = open("AoC\\2024\\D2\\D2_2024.txt","r")
    safe_reports = 0
    for row in data:
        values = []
        for num in row.split():
            values.append(int(num))

        safe = True
        if sorted(values) == values or sorted(values) == values[::-1]:
                i = 0
                while i<len(values)-1:
                    if abs(values[i]-values[i+1]) > 3 or values[i] == values[i+1]:
                        safe = False
                        i += 1
                    else:
                        i += 1
                if safe == True:
                    safe_reports += 1
    print(f"Part one: {safe_reports}")
    return

def main_P2():
    data = open("AoC\\2024\\D2\\D2_2024.txt","r")
    safe_reports = 0
    for row in data:
        values = []
        for num in row.split():
            values.append(int(num))

        if check_safe(values):
            safe_reports += 1
            continue

        for i in range(len(values)):
            modified_values = values[:i]+values[i+1:]
            if check_safe(modified_values):
                safe_reports += 1
                break


    print(f"Part two: {safe_reports}")
    return


def check_safe(values):
    for i in range(len(values)-1):
        difference = abs(values[i]-values[i+1])
        if difference > 3 or difference == 0:
            return False
    return values == sorted(values) or values == sorted(values, reverse=True)

main_P1()
main_P2()