# Converting Anagrams Given two strings A and B, find the minimum number of characters that need to be deleted from these 2 strings to make them anagrams of each other.

# An Anagram is defined as two strings that contain the same characters with the same frequency, but possibly in a different order. For example:
# "listen" and "silent" are Anagrams.
# "triangle" and "integral" are Anagrams.

# Input Format
# The first line of input contains T - the number of test cases. It's followed by T lines, each line contains 2 space separated strings - A and B.

# Output Format
# For each test case, print the minimum number of deletions, separated by a new line.

# Constraints
# 1 <= T <= 1000
# 1 <= len(A), len(B) <= 1000
# 'a' <= A[i], B[i] <= 'z'

# Example
# Input
# 2
# smart interviews
# data structures

# Output
# 9
# 12

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

for _ in range(int(input())):
    a, b = input().split()
    freq_a = Counter(a)
    freq_b = Counter(b)

    deletions = 0
    all_chars = set(freq_a.keys()).union(freq_b.keys())
    for char in all_chars:
        deletions += abs(freq_a.get(char, 0) - freq_b.get(char, 0))

    print(deletions)