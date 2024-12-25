filename = "full.txt"

import heapq

values = {}
sim_score = 0

with open(filename, "r") as file:
    lines = file.readlines()  # Reads one line from the file
    
    for line in lines:
        numbers = line.split()
        left_val, right_val = map(int, numbers)
        values[left_val] = 0
    for line in lines:
        numbers = line.split()
        left_val, right_val = map(int, numbers)
        if right_val in values:
            values[right_val] += 1
    for line in lines:
        numbers = line.split()
        left_val, right_val = map(int, numbers)
        sim_score += (left_val*values[left_val])
    
print(f"total_distance: {sim_score}")