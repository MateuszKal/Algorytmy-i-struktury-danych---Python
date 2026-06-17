from itertools import combinations

def knapsack_brute_force_solver(values, weights, capacity):
    best_value, best_combination = 0, None

    # Generate all possible combinations of items
    for combination in (combinations(range(len(values)), i) for i in range(len(values) + 1)):
        for combo in combination:
            total_weight = sum(weights[j] for j in combo)
            total_value = sum(values[j] for j in combo)

            if total_weight <= capacity and total_value > best_value:
                best_value, best_combination = total_value, combo

    return best_combination

def knapsack_dynamic_programming_solver(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            included_items.append(i-1)
            w -= weights[i-1]

    return included_items

def read_knapsack_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')

    capacity = int(lines[0])
    values, weights = zip(*[map(int, line.split(',')) for line in lines[2:]])

    return capacity, list(values), list(weights)

def execute_knapsack_algorithms(filename):
    capacity, values, weights = read_knapsack_data_from_file(filename)
    brute_force_result = knapsack_brute_force_solver(values, weights, capacity)
    dynamic_programming_result = knapsack_dynamic_programming_solver(values, weights, capacity)
    return brute_force_result, dynamic_programming_result

if __name__ == "__main__":
    filename = 'knapsack_29_capacity.txt'  # Replace with your file name
    brute_force_result, dynamic_programming_result = execute_knapsack_algorithms(filename)

    print("Brute Force Result:", brute_force_result)
    print("Dynamic Programming Result:", dynamic_programming_result)