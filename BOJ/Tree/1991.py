N = int(input())

def preOrder(tree, root):
    print(root, end='')
    if tree[root][0] != '.':
        preOrder(tree, tree[root][0])

    if tree[root][1] != '.':
        preOrder(tree, tree[root][1])

def inOrder(tree, root):
    if tree[root][0] != '.':
        inOrder(tree, tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inOrder(tree, tree[root][1])

def postOrder(tree, root):
    if tree[root][0] != '.':
        postOrder(tree, tree[root][0])
    if tree[root][1] != '.':
        postOrder(tree, tree[root][1])
    print(root, end='')

tree = {}
root = 'A'
for i in range(N):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]


preOrder(tree,root)
print()
inOrder(tree,root)
print()
postOrder(tree,root)


