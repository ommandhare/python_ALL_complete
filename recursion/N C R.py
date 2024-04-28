def combinations(N, R):
    # Base case: when either N or R is 0 or N equals R
    if R == 0 or N == R:
        return 1
    # Recursive case: compute combinations using Pascal's triangle identity
    return combinations(N - 1, R - 1) + combinations(N - 1, R)

def generate_combinations(N, R):
    if N < R:
        print("Invalid input: N should be greater than or equal to R.")
        return
    for i in range(N + 1):
        for j in range(min(i, R) + 1):
            if j == 0 or j == i:
                print(1, end=" ")
            else:
                print(combinations(i, j), end=" ")
        print()

# Getting input from the user
N = int(input("Enter the value of N: "))
R = int(input("Enter the value of R: "))

# Generating combinations
print(f"All possible combinations of {N} C {R}:")
generate_combinations(N, R)
