# H Pattern Given N - the height and M - the width, print the letter "H" using '*'.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by T lines, each line contains N - height space separated by M - width.

# Output Format
# For each test case, print the test case number as shown, followed by the H pattern, separated by a new line.

# Constraints
# 1 <= T <= 50
# 3 < M <= N < 100

# Example
# Input
# 3
# 3 3
# 6 5
# 5 3

# Output
# Case #1:* *
# ***
# * *
# Case #2:*   *
# *   *
# *****
# *   *
# *   *
# *   *
# Case #3:* *
# * *
# ***
# * *
# * *

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_h_pattern(test_case_num, N, M):
    print(f"Case #{test_case_num}:")

    mid = N // 2 - (1 if N % 2 == 0 else 0)

    for i in range(N):
        row = ''
        for j in range(M):
            if j == 0 or j == M - 1:
                row += '*'
            elif i == mid:
                row += '*'
            else:
                row += ' '
        print(row)

def main():
    T = int(input())
    for case in range(1, T + 1):
        N, M = map(int, input().split())
        print_h_pattern(case, N, M)

if __name__ == "__main__":
    main()