# Splitting String Given a string, find the minimum number of cuts needed to obtain a perfect string. A perfect string is a string that has only a single type of character. Example: aaaaa. 
# A cut in the string should be done exactly in the middle dividing the string into two equal halves.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single string consisting only of lowercase English alphabets.

# Output Format
# For each test case, print the minimum number of cuts required to get a perfect string, separated by a new line. If it is not possible to obtain a perfect string, print -1.

# Constraints
# 1 <= T <= 103
# 1 <= len(str) <= 104

# Example
# Input
# 2
# aacabbaa
# ab

# Output
# 2
# 1

# Explanation

# Example 1:
# Cut-1: [aaca][bbaa], Cut-2: [bb][aa]

# Example 2:
# Cut-1: [a][b]

def min_cuts(s):
    n = len(s)
    # If already perfect
    if s.count(s[0]) == n:
        return 0
    # If odd length, can't split in the middle
    if n % 2 != 0:
        return -1

    def helper(sub):
        m = len(sub)
        if sub.count(sub[0]) == m:
            return 0
        if m % 2 != 0:
            return -1
        mid = m // 2
        left = sub[:mid]
        right = sub[mid:]
        left_cuts = helper(left)
        right_cuts = helper(right)
        if left_cuts == -1 and right_cuts == -1:
            return -1
        # If either side is perfect, we only need to cut the other side
        if left_cuts == -1:
            return 1 + right_cuts
        if right_cuts == -1:
            return 1 + left_cuts
        return 1 + min(left_cuts, right_cuts)

    return helper(s)

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_cuts(s))
