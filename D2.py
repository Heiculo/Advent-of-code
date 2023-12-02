# AOC 2023 Day 2
# Eetu Heikurinen

# P1

def main():
    # Dictionary to specify maximum amounts
    Dict = {"red":12, "green":13, "blue": 14}
    ValidGames = []
    Sum = 0
    File = open("D2.txt","r")
    Row = File.readline().strip()
    while len(Row) > 0:
        Valid = True
        # Split ID and data
        ID, Row = Row.split(":")
        # Split different picks 
        for Set in Row.split(";"):
            # Split different colors in picks
            for Action in Set.split(","):
                Action = Action.split(" ")
                Amount = int(Action[1])
                Color = Action[2]
                # If the amount of cubes is larger than given values, break the loop
                if Amount > Dict.get(str(Color)):
                    Valid = False
                    break
        # If the amounts are lower save the game ID and read next line
        if Valid == True:
            ValidGames.append(ID)
        Row = File.readline().strip()
    for Game in ValidGames:
        # Split Game and ID and sum up the IDs
        Number = Game.split(" ")[1]
        Sum += int(Number)
    print(Sum)
main()


# P2

def main():
    Values = []
    File = open("D2.txt","r")
    Row = File.readline().strip()
    while len(Row) > 0:
        # Reset the values for each color for every row
        Dict = {"red":0, "green":0, "blue": 0}
        Row = Row.split(":")[1]
        for Set in Row.split(";"):
            for Action in Set.split(","):
                Action = Action.split(" ")
                Amount = int(Action[1])
                Color = Action[2]
                # If there is more cubes of a single color in a pick, update the value in the dictionary
                if Amount > Dict.get(str(Color)):
                    Dict[Color]=Amount
        # Save the product of the biggest values to a list
        Values.append(Dict["red"]*Dict["green"]*Dict["blue"])
        Row = File.readline().strip()
    Product = 0
    # Sum up the values in the products list
    for x in Values:
        Product += x
    print(Product)
main()
