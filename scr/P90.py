from itertools import combinations

# Generating all possible combinations of 6 digits
combinations = list(combinations(range(10), 6))

# Defining the pairs required to display all square numbers
required_pairs = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]

# Function to check if two sets can display all square numbers
def check_pairs(set1, set2):
    for pair in required_pairs:
        if not ((pair[0] in set1 and pair[1] in set2) or (pair[0] in set2 and pair[1] in set1)):
            return False
    return True

# Function to count the distinct arrangements
def count_arrangements():
    count = 0
    for i in range(len(combinations)):
        for j in range(i, len(combinations)):  # Avoid double counting
            # Turning 6 and 9 upside down
            set1 = set(combinations[i])
            set2 = set(combinations[j])
            if 6 in set1: set1.add(9)
            if 9 in set1: set1.add(6)
            if 6 in set2: set2.add(9)
            if 9 in set2: set2.add(6)
            if check_pairs(set1, set2):
                count += 1


    return count

print(count_arrangements())