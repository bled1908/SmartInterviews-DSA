# Height Reduction You are given the heights of N poles. You need to cut down at least K metres of pole but you are only allowed to cut all the poles at the same fixed height.

# Let's say you set a height parameter H, meaning you can cut off the portions of all poles that exceed H. For example, if the heights of the poles are 10, 13, 17, and 20 meters, and you set the cutting height at 15 meters, the new heights of the poles would be 10, 13, 15, and 15 meters respectively. This means you've removed 2 meters from the third pole and 5 meters from the fourth, which gives a total of 7 meters.

# Your task is to determine the maximum integer height H such that cutting all poles above this height results in at least K meters being reduced in total. If it’s not possible to reduce the total height by K meters, print -1.

# Input Format
# The first line of input contains T - number of test cases. The first line of each test case contains 2 integers, N - the number of poles and K - total length of poles that must be cut. The second line contains N integers - heights of the N poles.

# Output Format
# For each testcase, print the maximum integer height, separated by newline. Print -1 if you cannot cut at least K metres of pole.

# Constraints
# 30 points
# 1 <= N, K <= 103
# 1 <= ar[i] <= 103

# 70 points
# 1 <= N, K <= 105
# 1 <= ar[i] <= 106

# General Constraints
# 1 <= T <= 100

# Example
# Input
# 2
# 5 15
# 7 8 10 20 3
# 4 6
# 10 1 3 2

# Output
# 7
# 4

# Explanation

# For example-1, if we cut all the poles at H=7, then we are able to cut 0,1,3,13,0 metres of pole respectively, giving a reduction of 0+1+3+13+0 = 17 >= 15.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_cut_height(n, k, heights):
    low, high = 0, max(heights)
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        total_cut = sum((h - mid) for h in heights if h > mid)

        if total_cut >= k:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer


for _ in range(int(input())):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    print(max_cut_height(n, k, heights))
    