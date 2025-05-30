# Reverse String Leaving Special Characters Given a string A, composed of lowercase alphabets and special characters, your goal is to reverse the given string ensuring that the special characters retain their initial positions.

# Input Format
# First line of input contains T - number of test cases. Its followed by T lines, each line contains a string of size N, containing only lowercase english alphabets and special characters.

# Output Format
# For each test case, reverse the string leaving special characters in same place and print the reversed string, separated by newline.

# Constraints
# 1 <= T <= 100
# 1 <= len(A) <= 104

# Example
# Input
# 3
# ma#$da%m$
# %dog#of%
# dou&b$le%

# Output
# ma#$da%m$
# %fog#od%
# elb&u$od%

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    s = input()
    letters = [c for c in s if c.isalpha()]
    reversed_letters = letters[::-1]
    
    result = []
    letter_index = 0

    for char in s:
        if char.isalpha():
            result.append(reversed_letters[letter_index])
            letter_index += 1
        else:
            result.append(char)
    
    print("".join(result))