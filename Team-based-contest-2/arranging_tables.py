# Arranging Tables In a restaurant, there are N groups waiting to have dinner. Each group will have at least 1 and at most 4 people. A table has only 4 seats. The restaurant owner wants to arrange a minimum number of tables so that all the groups can have their dinner. However, people of the same group want to sit at the same table and at the same time a table can have multiple groups. Help the restaurant owner to find the minimum number of tables required.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the number of groups waiting to have their dinner and the second line contains N integers where ith number denotes the number of people in the ith group.

# Output Format
# For each test case, print the minimum number of tables required, separated by a new line.

# Constraints
#  1 <= T <= 100 
#  1 <= N <= 104

# Example
# Input
#  2
#  5
#  1 2 4 3 3 
#  8
#  2 3 4 4 2 1 3 1 

# Output
#  4
#  5

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

for _ in range(int(input())):
    n = int(input())
    groups = list(map(int, input().split()))

    count = [0] * 5
    for g in groups:
        count[g] += 1
    
    tables = 0

    tables += count[4]

    pair_3_1 = min(count[3], count[1])
    tables += count[3]
    count[1] -= pair_3_1

    tables += count[2] // 2
    count[2] %= 2

    if count[2]:
        tables += 1
        count[1] -= min(2, count[1])

    if count[1] > 0:
        tables += math.ceil(count[1] / 4)
    
    print(tables)