# Eetu Heikurinen
# 1.12.2025, AoC 2025 Day 1


class SafeCounter:
    def __init__(self, value=50):
        self.value = value % 100  # Force the correct range (0-99)
        self.zeros = 0 # Part 1
        self.zero_passes = 0 # Part 2
    
    def move(self, command):
        command = command.strip().upper()

        # Parsing digits
        direction = command[0]
        steps = int(command[1:])
        old_value = self.value
        
        if direction == "R":
            # Count the zeros on each click to the right
            for i in range(1,steps+1):
                if (old_value + i) % 100 == 0:
                    self.zero_passes += 1
            self.value = (old_value + steps) % 100


        elif direction == "L":
            # Count the zeros on each click to the left
            for i in range(1,steps+1):
                if (old_value - i) % 100 == 0:
                    self.zero_passes += 1
            self.value = (old_value - steps) % 100

        # Check if the dial ends up on 0
        if self.value == 0:
            self.zeros += 1
    
    def get_zeros(self):
        return self.zeros
    
    def get_zero_passes(self):
        return self.zero_passes

def process_file(filename, start_value=50):
    dial = SafeCounter(start_value)

    with open(filename, "r") as f:
        for line in f:
            cmd = line.strip()
            if cmd:
                dial.move(cmd)

    return dial.get_zeros(), dial.get_zero_passes()

def main_P1():
    zero_hits1, __ = process_file(r"AoC\2025\D1\D1_2025.txt")
    print("Final answer P1: ",zero_hits1)

def main_P2():
    __, zero_passes2 = process_file(r"AoC\2025\D1\D1_2025.txt")
    print("Final answer P2: ",zero_passes2)

main_P1()
main_P2()
