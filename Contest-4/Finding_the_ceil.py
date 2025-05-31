# Finding the Ceil Given an array, you have to find the ceil of a number x. The ceil of a number x is nothing but the smallest number in the array greater than or equal to x.

# Input Format
# The first line of input contains the N-size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the ceil of X in the given array.

# Output Format
# For each query, print the ceil of X, separated by a new line. If ceil is not found, print the value of "INT_MAX".

# Constraints
# 30 points
# 1 <= N <= 105
# 1 <= Q <= 102
# -108 <= ar[i] <= 108

# 70 points
# 1 <= N <= 105
# 1 <= Q <= 105
# -108 <= ar[i] <= 108

# Example
# Input
# 6
# -6 10 -1 20 15 5
# 5
# -1
# 10
# 13
# 25
# -10

# Output
# -1
# 10
# 15
# 2147483647
# -6

# Explanation

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
INT_MAX = 2147483647
def find_ceil(arr, n, k):                                 
    ans = INT_MAX
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            ans = arr[mid]
            break
        if arr[mid] > k:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans
    

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(int(input())):
    q = int(input())
    print(find_ceil(arr, n, q))