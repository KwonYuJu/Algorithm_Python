N = int(input())
tree = {}   # 딕셔너리로 트리 구현
for i in range(N):
    root, left, right = input().split()     # 루트, 왼쪽자식, 오른쪽자식
    tree[root] = left, right    # {'A': ('B', 'C')}

def preorder(v):    # 전위순회 (본왼우)
    if v != '.':    # .이 아니면 -> 자식노드가 있다면
        print(v, end='')        # 본, 루트 출력
        preorder(tree[v][0])    # 왼, 왼쪽노드 재귀 탐색
        preorder(tree[v][1])    # 우, 오른쪽노드 재귀 탐색

def inorder(v):     # 중위순회 (왼본우)
    if v != '.':    # 자식노드가 있다면
        inorder(tree[v][0])     # 왼
        print(v, end='')        # 본
        inorder(tree[v][1])     # 우

def postorder(v):   # 후위순회 (왼우본)
    if v != '.':    # 자식노드가 있다면
        postorder(tree[v][0])   # 왼
        postorder(tree[v][1])   # 우
        print(v, end='')        # 본

# 루트노드 'A'
preorder('A')   # 전위
print()
inorder('A')    # 중위
print()
postorder('A')  # 후위
