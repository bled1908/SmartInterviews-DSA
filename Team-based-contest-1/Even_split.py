# Even Split Given a number N, check if you can split the number into 2 non-zero even parts.

# Input Format
# First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N.

# Output Format
# For each test case, print "Yes" if you can split the number into 2 non-zero even parts, "No" otherwise, separated by new line.

# Constraints
# 1 <= T <= 105
# 0 <= N <= 1018

# Example
# Input
# 2
# 8
# 5

# Output
# Yes
# No

# Explanation

# Example 1:
# You can split 8 as 4,4 or 6,2.

# Example 2:
# You cannot split 5 into 2 even parts.

# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    print("Yes" if n % 2 == 0 and n > 2 else "No")