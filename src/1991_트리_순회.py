N = int(input())
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.data)

def preorder(node):
    print(node, end = "")
    if node.left != '.':
        preorder(bt[node.left])
    if node.right != '.':
        preorder(bt[node.right])

def inorder(node):
    if node.left != '.':
        inorder(bt[node.left])
    print(node, end = '')
    if node.right != '.':
        inorder(bt[node.right])

def postorder(node):
    if node.left != '.':
        postorder(bt[node.left])
    if node.right != '.':
        postorder(bt[node.right])
    print(node, end = '')
bt = {}


for _ in range(N):
    data, left, right = input().split()
    bt[data] = Node(data, left, right)

preorder(bt['A'])
print()
inorder(bt['A'])
print()
postorder(bt['A'])
print()