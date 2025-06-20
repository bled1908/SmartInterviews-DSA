# Range Queries Given an array of N integers in the range 0 to K, answer queries of the form [a,b] - How many integers fall in the range [a,b] ?

# Input Format
# The first line of input contains T - the number of test cases. The first line of each test case contains N - the size of the array and K - the range of array elements. It's followed by N integers in the range 0 to K - the elements of the array. The next line of each test case contains Q - the number of queries. It's followed by Q lines containing 2 integers a and b - the range of the query.

# Output Format
# For each test case, for each query, print the number of integers in the range [a,b], separated by newline.

# Constraints
# 30 points
# 1 <= T <= 200
# 1 <= N, Q, K <= 103
# 0 <= a <= b <= K

# 70 points
# 1 <= T <= 200
# 1 <= N, Q, K <= 104
# 0 <= a <= b <= K

# Example
# Input
# 2
# 4 20
# 12 0 15 9
# 3
# 5 10
# 1 7
# 12 15
# 10 5
# 5 4 2 5 2 4 5 1 3 3
# 5
# 1 5
# 5 5
# 1 1
# 3 5
# 2 4

# Output
# 1
# 0
# 2
# 10
# 3
# 1
# 7
# 6

# Explanation

# Example 1:
 
# First Query: Output is 1 because 9 is the only element in the given array that lies in the interval [5, 10]
# Second Query: Output is 0 because there are no elements in the given array which lies in the interval [1, 7]
# Third Query: Output is 2 because 12,15 are the elements in the given array which lies in the interval [12, 15]

# Enter your code here. Read input from STDIN. Print output to STDOUT
def process_test_case(n, k, arr, queries):
    freq = [0] * (k + 1)
    for num in arr:
        freq[num] += 1
    
    prefix = [0] * (k + 1)
    prefix[0] = freq[0]
    for i in range(1, k + 1):
        prefix[i] = prefix[i - 1] + freq[i]
    
    results = []
    for a, b in queries:
        if a > 0:
            results.append(prefix[b] - prefix[a - 1])
        else:
            results.append(prefix[b])
    return results

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    results = process_test_case(n, k, arr, queries)
    for res in results:
        print(res)