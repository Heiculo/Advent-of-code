# Eetu Heikurinen
# 1.12.2024, AoC 2024 Day 1

from collections import Counter

def main_P1():
    left_list = []
    right_list = []
    data = open("AoC\\2024\\D1\\D1_2024.txt","r")
    
    for row in data:
        left, right = row.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    difference = 0
    # take the absolute value of each corresponding element and add them up
    for i in range(0,len(left_list)):
        difference += abs(left_list[i]-right_list[i])

    print(f"Difference: {difference}")

    return left_list, right_list

def main_P2(left_list, right_list):
    # A dictionary of how many times each number appears on right side
    right_appearances = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        if num in right_appearances:
            similarity_score += num*right_appearances[num]
    print(f"Similarity score: {similarity_score}")

left_list, right_list = main_P1()
main_P2(left_list, right_list)

    
