# Check Anagrams Given 2 strings, check if they are anagrams. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutations of string A must be the same as string B.

# Input Format
# The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated strings.

# Output Format
# For each test case, print True/False, separated by a new line.

# Constraints
# 10 points
# 1 <= T <= 100
# 1 <= len(S) <= 103
# 'a' <= S[i] <= 'z'

# 40 points
# 1 <= T <= 100
# 1 <= len(S) <= 105
# 'a' <= S[i] <= 'z'

# Example
# Input
# 4
# iamlordvoldemort tommarvoloriddle
# b h
# stop post
# hi hey

# Output
# True
# False
# True
# False

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
def anagrams(s, t):
    if len(s) != len(t):
        return False

    freq1 = {}
    freq2 = {}
    for char in s:
        freq1[char] = freq1.get(char, 0) + 1
    for char in t:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2

for _ in range(int(input())):
    s, t = input().split()
    s = s.strip()
    t = t.strip()
    res = anagrams(s, t)
    print("True" if res else "False")
    
    