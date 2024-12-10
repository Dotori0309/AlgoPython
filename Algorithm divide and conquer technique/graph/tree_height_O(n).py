class TNode:						# 이진트리를 위한 노드 클래스
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

def calc_height(root) :			# 루트노드 root
    if root is None : 				# 공백 트리이면 --> 0을 반환
        return 0					#  높이가 0 --> 0을 반환
    hLeft = calc_height(root.left)	# 왼쪽 트리의 높이 --> hLeft
    hRight = calc_height(root.right) # 오른쪽 트리의 높이 --> hRight
    return max(hLeft,hRight) + 1	# 더 높은 높이에 1을 더해 반환.

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)		# 루트 노드
print(" 트리의 높이 =", calc_height(root))

