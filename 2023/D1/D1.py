# AOC 2023 Day 1
# Eetu Heikurinen

# P1
def main():
    File = open("D1.txt","r")
    # split the file into rows
    Row = File.readline()
    Sum = 0
    while len(Row)>0:
        # Make a new list for digits in the row
        Numbers = []
        for Char in Row:
           # If a charachter is a digit add it to the list
           if Char.isdigit():
            Numbers.append(Char)
            # Put the first and last togehter
            Combined = Numbers[0]+Numbers[-1]
        # Add it to the sum and read the next line
        Sum += int(Combined) 
        Row = File.readline()
    print(Sum)
    return None

main()



# P2
def main():
    File = open("D1.txt","r")
    Row = File.readline()
    # Create a dictionary where keys are numbers written in letters
    Numeric = [1,2,3,4,5,6,7,8,9]
    Written = ["one","two","three","four","five","six","seven","eight","nine"]
    Dict = {}
    i = 0
    for x in Numeric:
        Dict[Written[i]] = Numeric[i]
        i += 1
    
    Sum = 0
    while len(Row)>0:
        Numbers = []
        for Key in Dict:
            if Key in Row:
                # If a word for a number appears, switch it and add the word to both sides of the number
                # To not disturb the spelling of some combined numbers. For example (eighthree)
                Row = Row.replace(Key,str(Key)+str(Dict[Key])+str(Key))
        for Char in Row:
            # Same structure as in Pt 1
            if Char.isdigit():
                Numbers.append(Char)
        
        Combined = str(Numbers[0])+str(Numbers[-1])
        Sum += int(Combined) 
        Row = File.readline()
    print(Sum)
    return None

main()