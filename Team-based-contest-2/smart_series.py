# Smart Series Given an integer N, find the maximum sum that you can get from the following series: 1*2 - 2*3 + 3*4 - 4*5 .... K*(K+1), where K<=N.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by T lines, each contains a single integer N.

# Output Format
# For each test case, print the result, separated by a newline.

# Constraints
# 30 points
# 1 <= T <= 100
# 1 <= N <= 100

# 70 points
# 1 <= T <= 105
# 1 <= N <= 109

# Example
# Input
# 2
# 3
# 5

# Output
# 8
# 18

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    m = n + n % 2  # If n is odd, m = n+1; if n is even, m = n
    max_sum = (m ** 2) // 2
    print(max_sum)
