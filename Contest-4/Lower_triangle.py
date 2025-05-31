# Lower Triangle Given a square matrix of size N × N, find the sum of its lower triangle elements. 

# Input Format
#  The first line of input contains N - the size of the matrix. It is followed by N lines each containing N integers - elements of the matrix.

# Output Format
#  Print the sum of the lower triangle of the matrix. 

# Constraints
#  1 <= N <= 100
#  -105 <= ar[i] <= 105

# Example
# Input
#  3
#  5 9 -2 
#  -3 4 1 
#  2 6 1 

# Output
#  15

# Explanation

#  The sum of the lower triangle matrix is 5 - 3 + 4 + 2 + 6 + 1 = 15.

# Enter your code here. Read input from STDIN. Print output to STDOUT

mat = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

sum1 = 0
for i in range(n):
    for j in range(i + 1):
        sum1 += mat[i][j]
print(sum1)