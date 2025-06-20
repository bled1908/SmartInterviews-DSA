# Print Hollow Diamond Pattern Print a hollow diamond pattern using '*'. See examples for more details.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.

# Output Format
# For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.

# Constraints
# 1 <= T <= 100
# 3 <= N <= 201

# Example
# Input4
# 3
# 7
# 5
# 15

# OutputCase #1:
#  *
# * *
#  *
# Case #2:
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
# Case #3:
#   *
#  * *
# *   *
#  * *
#   *
# Case #4:
#        *
#       * *
#      *   *
#     *     *
#    *       *
#   *         *
#  *           *
# *             *
#  *           *
#   *         *
#    *       *
#     *     *
#      *   *
#       * *
#        *
# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_hollow_diamond(n):
    # for upper half
    for i in range(n // 2 + 1):
        if i == 0:
            print(" " * (n // 2) + "*")
        else:
            print(" " * (n // 2 - i) + "*" + " " * (2 * i - 1) + "*")
    # for lower half
    for i in range(n // 2 - 1, -1 , -1):
        if i == 0:
            print(" " * (n // 2) + "*")
        else:
            print(" " * (n // 2 - i) + "*" + " " * (2 * i - 1) + "*")
    

for t in range(int(input())):
    n = int(input())
    print(f"Case #{t + 1}:")
    print_hollow_diamond(n)