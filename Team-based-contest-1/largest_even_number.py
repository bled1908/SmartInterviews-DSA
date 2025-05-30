# Largest Even Number In the given string A, comprising letters, digits, and special characters, your objective is to generate the highest possible even number by eliminating duplicate digits.

# Input Format
# First line of input contains T - number of test cases. Its followed by T lines, each line contains a string of size N.

# Output Format
# For each test case, produce the largest even number and print it, separated by newline. If no such number exists, print -1.

# Constraints
# 1 <= T <= 1000
# 1 <= len(A) <= 104

# Example
# Input
# 3
# sma23@#rt372*
# 39^%735int1
# sna789%67p$56

# Output
# 732
# -1
# 98756

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    s = input()
    digits = set(c for c in s if c.isdigit())
    digits = sorted(digits, reverse = True)

    even_digits = [d for d in digits if int(d) % 2 == 0]

    if not even_digits:
        print(-1)
    else:
        smallest_even = min(even_digits)
        digits.remove(smallest_even)
        result = "".join(digits) + smallest_even
        print(result)