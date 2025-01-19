n = int(input())
tree = dict()
for _ in range(n):
    tmp = input().split()
    tree[tmp[0]] = [tmp[1], tmp[2]]

def inorder(dic, start):
    print(start, end='')
    left, right = dic[start][0], dic[start][1]
    if left != '.':
        inorder(dic, left)
    if right != '.':
        inorder(dic, right)

def preorder(dic, start):
    if start != '.':
        left, right = dic[start][0], dic[start][1]
        preorder(dic, left)
        print(start, end='')
        preorder(dic, right)

def postorder(dic, start):
    if start != '.':
        left, right = dic[start][0], dic[start][1]
        postorder(dic, left)
        postorder(dic, right)
        print(start, end='')

inorder(tree, 'A')
print('')
preorder(tree, 'A')
print('')
postorder(tree, 'A')