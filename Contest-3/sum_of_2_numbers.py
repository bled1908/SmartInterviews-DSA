# Sum of 2 Numbers Given an array, check if there exist 2 elements of the array such that their sum is equal to the sum of the remaining elements of the array.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains N integers - elements of the array.

# Output Format
# For each test case, print "Yes" if such elements exist, and "No" otherwise, separated by a new line.

# Constraints
# 30 points
# 1 <= T <= 100
# 1 <= N <= 1000
# -106 <= A[i] <= 106

# 70 points
# 1 <= T <= 500
# 1 <= N <= 10000
# -106 <= A[i] <= 106

# Example
# Input
# 2
# 5
# -3 5 8 2 -4
# 6
# 5 -10 8 4 2 -3

# Output
# Yes
# No

# Explanation

# Example 1:
# Possible values: 8 + (-4) = (-3) + 5 + 2.

# Example 2:
# No 2 elements exist whose sum is equal to the sum of the remaining array elements.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_of_2(arr, n):
    sum1 = sum(arr)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if arr[p1] + arr[p2] == (sum1 - arr[p1] - arr[p2]):
            return True
        elif arr[p1] + arr[p2] < (sum1 - arr[p1] - arr[p2]):
            p1 += 1
        else:
            p2 -= 1
    return False

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print("Yes" if sum_of_2(arr, n) else "No")