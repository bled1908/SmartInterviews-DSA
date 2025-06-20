# Longest Substring with Max K Vowels Given a string S and an integer K, print the length of the longest substring which contains at most K vowels.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains K - the max number of vowels and the second line contains a string of size N.

# Output Format
# For each test case, print the length of the longest substring which contains at most K vowels, separated by newline.

# Constraints
# 10 points
# 1 <= N <= 102

# 20 points
# 1 <= N <= 103

# 70 points
# 1 <= N <= 104

# General Constraints
# 1 <= T <= 100
# 0 <= K <= N
# 'a' <= s[i] <= 'z'

# Example
# Input
# 3
# 2
# smartinterviews
# 1
# algorithms
# 2
# searching

# Output
# 8
# 6
# 7

# Explanation

# Test Case 1:
# We have 2 substrings of length 8 which have at most 2 vowels: "smartint", "rtinterv"

# Test Case 2:
# We have a substring of length 6 which has at most 1 vowel: "rithms"

# Test Case 3:
# We have a substring of length 7 which has at most 2 vowels: "arching"

# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_vowel(c):
    return c in 'aeiou'

def long_substring(k, s):
    n = len(s)
    start = 0
    vowel_count = 0
    max_len = 0

    for end in range(n):
        if is_vowel(s[end]):
            vowel_count += 1

        while vowel_count > k:
            if is_vowel(s[start]):
                vowel_count -= 1
            start += 1
        
        max_len = max(max_len, end - start + 1)
    
    return max_len


for _ in range(int(input())):
    k = int(input())
    s = input().strip()
    print(long_substring(k, s))