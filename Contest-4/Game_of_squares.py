# Game of Squares Alice and Bob are playing a game. They are given a number N. They make moves, in turn, Alice playing first. Each move consists of subtracting a perfect square (not less than 1) from the number, the player who faces 0 loses. You are given a number N, and you have to find out whether Alice can win the game, if both Alice and Bob play optimally.

# Input Format
# The first line contains T - the number of test cases. The next T lines contain a number N.

# Output Format
# For each test case, print "Win" if Alice can win the game, or else print "Lose", separated by a newline.

# Constraints
# 1 <= T, N <= 105

# Example
# Input
# 5
# 1
# 2
# 3
# 16
# 10

# Output
# Win
# Lose
# Win
# Win
# Lose

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
max_n = int(1e5)
perfect_squares = [i * i for i in range(1, max_n)]
optimal = [False] * (max_n + 1)
for i in range(1, max_n + 1):
    for per in perfect_squares:
        if per > i:
            break
        elif not optimal[i - per]:
            optimal[i] = True

for _ in range(int(input())):
    n = int(input())
    print("Win" if optimal[n] else "Lose")