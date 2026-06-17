
import os
import random

def generate_knapsack_file(filename, num_items, capacity):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)

    with open(file_path, 'w') as f:
        f.write(f"{capacity}\n")
        f.write(f"{num_items}\n")
        for _ in range(num_items):
            value = random.randint(0, 100)
            weight = random.randint(0, 100)
            f.write(f"{value}, {weight}\n")

for capacity in range(1, 30, 2):
    filename = f'knapsack_{capacity}_capacity.txt'
    generate_knapsack_file(filename, 30, capacity)
