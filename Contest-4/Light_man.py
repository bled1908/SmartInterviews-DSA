# Light Man One fine evening, Light Man was walking down the streets of Hogwarts. Light Man is a new hero in the wizarding community with the power to manipulate light. Now, he decided to test his superpowers on the street lights. His power allows him to choose a single light at a time and change its state: ON<->OFF. As he is running late for his next adventure, he can only use his power for a maximum of M times. Now, given the initial state of the street lights:
# 1 - ON
# 0 - OFF
# You have to find the maximum continuous series of street lights in the ON state after Light Man has performed a maximum of M spells.

# Input Format
# The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line of each test case contains N, M - the total number of street lights and the maximum number of spells, and the second line contains the state of the lights.

# Output Format
# For each test case, print the length of the maximum continuous series of lights in ON state after Light Man performs a maximum of M spells, separated by newline.

# Constraints
# 10 points
# 1 <= T <= 100
# 1 <= N <= 100

# 20 points
# 1 <= T <= 100
# 1 <= N <= 1000

# 70 points
# 1 <= T <= 100
# 1 <= N <= 100000

# General Constraints
# 0 <= M <= N
# 0 <= ar[i] <= 1

# Example
# Input
# 5
# 8 1
# 1 0 0 0 0 0 1 1
# 2 1
# 1 0
# 8 7
# 1 1 0 1 1 0 1 0
# 17 4
# 0 1 1 0 0 0 1 1 0 1 1 0 1 0 1 0 1
# 35 13
# 1 0 1 1 1 1 1 1 1 0 0 1 0 0 0 1 0 0 0 0 0 1 1 0 0 0 1 0 1 1 1 0 1 0 0

# Output
# 3
# 2
# 8
# 11
# 25

# Explanation

# Test Case 1: Light Man has 1 spell to use. He can use it to change one of the lights from OFF to ON, making the states of the lights as [1 0 0 0 0 1 1 1]. The maximum continuous series of lights in the ON state is 3.

# Test Case 2: Light Man has 1 spell and 2 street lights. He can use his spell to change the second light from OFF to ON, making the states of the lights as [1 1]. The maximum continuous series of lights in the ON state is 2.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_continuous_ones(arr, n, m):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(n):
        if arr[right] == 0:
            zero_count += 1

        while zero_count > m:
            if arr[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = max_continuous_ones(arr, n , m)
    print(res)