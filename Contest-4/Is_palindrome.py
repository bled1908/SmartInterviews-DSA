# Is Palindrome You are given a string S. You need to form a string K by picking vowels either from left to right or from right to left and check if K is a palindrome.

# Input Format
# The first and only line of input contains a string S.

# Output Format
# Print Yes if K is a palindrome, otherwise print No.

# Constraints
# 1 <= S.length() <= 1000
# 'a' <= S[i] <= 'z'

# Example
# Input
# rasengan

# Output
# Yes

# Explanation

# S = rasengan
# K (from left to right): aea
# K is a palindrome, hence the output is "Yes"

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
vowels = [v for v in s if v in ['a', 'e', 'i', 'o', 'u']]
print("Yes" if vowels == vowels[::-1] else "No")