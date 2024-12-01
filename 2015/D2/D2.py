# Eetu Heikurinen
# 10.10.2024

import numpy

def main():
    fname = "AoC\\2015\\D2\\D2_2015.txt"
    file = open(fname, "r")
    data = file.read().splitlines()
    paper = 0
    ribbon = 0
    for row in data:
        dimensions = [int(side) for side in row.split("x")]
        sorted_dimensions = sorted(dimensions)
        paper += 2*dimensions[0]*dimensions[1] + 2*dimensions[1]*dimensions[2]+2*dimensions[0]*dimensions[2]+sorted_dimensions[0]*sorted_dimensions[1]
        ribbon += 2*(sorted_dimensions[0]+sorted_dimensions[1])+numpy.prod(dimensions)


    print(f"Part 1: Paper: {paper}")
    print(f"Part 2: Ribbon: {ribbon}")
    
        
main()