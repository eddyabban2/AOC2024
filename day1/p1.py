filename = "full.txt"

import heapq

min_heap_left = []
min_heap_right = []
total_distance = 0

with open(filename, "r") as file:
    lines = file.readlines()  # Reads one line from the file
    for line in lines:
        numbers = line.split()
        left_val, right_val = map(int, numbers)
        heapq.heappush(min_heap_left, left_val)
        heapq.heappush(min_heap_right, right_val)
    while(len(min_heap_left) and len(min_heap_right)):
        total_distance += abs((heapq.heappop(min_heap_left) - heapq.heappop(min_heap_right)))
    
print(f"total_distance: {total_distance}")