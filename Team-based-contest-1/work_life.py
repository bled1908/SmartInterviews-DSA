# Work Life Bob works for support project where he has to resolve tickets every day. He knows number of tickets to resolve for next N days. Bob is struggling to balance his work life. On some days, workload is huge and on other days, it is very little. Now he can procrastinate and choose to postpone up to K tickets to next day (every day). However, a single ticket can be postponed at max once. Find optimal solution where workload can be distributed as evenly as possible and print the maximum number of tickets he needs to resolve on a day.

# Input Format
# First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains two integers, N - number of days and K - maximum number of tickets which can be postponed to next day. Second line contains N numbers - number of incoming tickets per day, separated by space.

# Output Format
# For each test case, print the maximum number of tickets he needs to resolve on a day, separated by newline.

# Constraints
# 1 <= T <= 100
# 1 <= N, K <= 104
# 1 <= A[i] <= 105

# Example
# Input
# 2
# 5 3
# 10 2 4 8 5
# 6 10
# 15 11 3 5 1 6

# Output
# 7
# 9

# Explanation

# Test Case 1:
# Day-1 = 10 tickets, he moves 3 tickets to Day-2, so Day-1's workload = 7 tickets.
# Day-2 = 3 (from Day-1) + 2 (from Day-2) = 5 tickets.
# Day-3 = 0 (from Day-2) + 4 (from Day-3) = 4 tickets.
# Day-4 = 0 (from Day-3) + 8 (from Day-4) = 8 tickets, we move 1 ticket to Day-5, so Day-4's workload = 7 tickets.
# (Note that he can even move 2 tickets from Day-4 to Day-5, making Day-4's workload = 6 and Day-5's workload = 7)
# Day-5 = 1 (from Day-4) + 5 (from Day-5) = 6 tickets.

# So final workload is [7,5,4,7,6] and maximum workload in a day is 7.

# Test Case 2:
# The best possible combination can be [7,7,7,7,7,7]. However, he cannot postpone Day-1's tickets to beyond Day-2, Day-2's tickets to beyond Day-3 and so on.

# One of the best possible ways to distribute the work load is:
# Day-1 = 15 tickets, he moves 6 tickets to Day-2, so Day-1's workload = 9 tickets.
# Day-2 = 6 (from Day-1) + 11 (from Day-2) = 17 tickets. He completes 6 tickets of Day-1 and 3 tickets from Day-2, moving 8 tickets of Day-2 to Day-3, so Day-2's workload = 3+6 = 9 tickets.
# Day-3 = 8 (from Day-2) + 3 (from Day-3) = 11 tickets. He completes 8 tickets of Day-2 and 1 ticket from Day-3, moving 2 tickets of Day-3 to Day-4, so Day-3's workload = 8+1 = 9 tickets.
# Day-4 = 2 (from Day-3) + 5 (from Day-4) = 7 tickets.

# So final workload is [9,9,9,7,1,6] and maximum workload in a day is 9.

def can_distribut_tickets(n, k, a, max_load):
    carry = 0
    for i in range(n):
        total_tickets = carry + a[i]
        if carry > max_load:
            return False
        tickets_to_resolve = min(total_tickets, max_load)
        tickets_from_day_i = max(0, tickets_to_resolve - carry)
        postponed = a[i] - tickets_from_day_i
        if postponed > k:
            return False
        carry = postponed
    return carry == 0

def solve_test_case():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_tickets = sum(a)
    low = (total_tickets + n - 1) // n
    high = total_tickets

    result = high
    while low <= high:
        mid = (low + high) // 2
        if can_distribut_tickets(n, k, a, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

t = int(input())
for _ in range(t):
    print(solve_test_case())