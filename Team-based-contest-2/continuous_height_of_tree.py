# Continuous Height of Tree Given an array of unique elements, construct a Binary Search Tree. After inserting every new node, print the height of the tree.

# Input Format
# First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

# Output Format
# For each test case, print the height of the Binary Search Tree after every insertion, separated by newline.

# Constraints

# 1 <= T <= 500
# 0 <= ar[i] <= 105

# 30 points
# 1 <= N <= 100

# 70 points
# 1 <= N <= 10000

# Example
# Input
# 3
# 5
# 1 2 3 4 5
# 5
# 3 2 4 1 5
# 7
# 4 5 15 0 1 7 17

# Output
# 0 1 2 3 4 
# 0 1 1 2 2 
# 0 1 2 2 2 3 3 

# Explanation 

# Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

def insert(root, key):
    if root is None:
        return Node(key), 0

    if key < root.key:
        root.left, _ = insert(root.left, key)
    else:
        root.right, _ = insert(root.right, key)

    left_height = root.left.height if root.left else -1
    right_height = root.right.height if root.right else -1
    root.height = max(left_height, right_height) + 1
    return root, root.height

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for val in arr:
        root, h = insert(root, val)
        print(h, end = ' ')
    print()