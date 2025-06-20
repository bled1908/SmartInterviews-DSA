# Sum and XOR Given an integer N, find the number of positive integers X such that X <= N and N+X=N^X (N xor X).

# Input Format
# The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N.

# Output Format
# For each test case, print the count of X's, separated by a newline.

# Constraints
# 30 points
# 1 <= T <= 103
# 0 <= N <= 103

# 70 points
# 1 <= T <= 104
# 0 <= N <= 1018

# Example
# Input
# 2
# 5
# 10

# Output
# 1
# 3

# Explanation

# Example 1
# Possible values: 5+2 = 5^2.

# Example 2
# Possible values: 10+1 = 10^1, 10+4=10^4, 10+5=10^5

def count_valid_x(n):
    if n == 0:
        return 0  # No positive integers satisfy the condition for N = 0
    count = 0
    temp_n = n  # Use temporary variable to avoid modifying the original n
    while temp_n:
        if (temp_n & 1) == 0:
            count += 1
        temp_n >>= 1
    return (1 << count) - 1  # Subtract 1 to exclude X = 0

for _ in range(int(input())):
    n = int(input())
    print(count_valid_x(n))