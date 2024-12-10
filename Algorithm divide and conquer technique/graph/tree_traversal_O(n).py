class TNode:						# 이진트리를 위한 노드 클래스
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

def preorder(n) :					# 전위 순회 함수
    if n is not None :
        print(n.data, end=' ')		# 먼저 루트노드 처리(화면 출력)
        preorder(n.left)			# 왼쪽 서브트리 처리
        preorder(n.right)			# 오른쪽 서브트리 처리

def inorder(n) :					# 중위 순회 함수
    if n is not None :
        inorder(n.left)			# 왼쪽 서브트리 처리
        print(n.data, end=' ')		# 루트노드 처리(화면 출력)
        inorder(n.right)			# 오른쪽 서브트리 처리

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)		# 루트 노드

print('   In-Order : ', end='')
inorder(root)
print()
print('  Pre-Order : ', end='')
preorder(root)
print()
print(' Post-Order : ', end='')
postorder(root)
print()

