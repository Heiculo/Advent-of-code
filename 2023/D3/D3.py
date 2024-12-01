# AOC 2023 Day 3
# Eetu Heikurinen

# P1
def main():
    Rows = []
    File = open("D3Testi.txt","r")
    Row = File.readline().strip()
    while len(Row)>0:
        Rows.append(Row)
        Row = File.readline().strip()

    print(Rows)
    return None

main()