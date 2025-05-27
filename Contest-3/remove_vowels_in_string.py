# Remove Vowels in String Given a string S of size N, create a new string T by removing all vowels from S while preserving the order of other characters. There will be atleast one consonant in string S.

# Input Format
# The first line of input contains an integer N. The second line of input contains string S.

# Output Format
# Print the string T.

# Constraints
# 1 <= N <= 1000
# 'a' <= S <= 'z'

# Example
# Input
# 15
# smartinterviews

# Output
# smrtntrvws

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
str1 = input()
res = []
vowels = ['a', 'e', 'i', 'o', 'u']
for s in str1:
    if s in vowels:
        continue
    else:
        res.append(s)
print("".join(res))