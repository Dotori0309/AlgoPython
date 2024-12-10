# set
# 순서가 보장되지 않음
# 인덱스로 엑세스 불가

A = {'돈가스', '보쌈', 3}
B = {'짬뽕', '초밥', 3}
D = {1: '돈가스', 2: '보쌈', 3: '짬뽕'}


print(A, type(A))
print(B, type(B))
print(A.union(B))
print(A.difference(B))
print(A.intersection(B))
# print(A[1])
print(D, type(D))
print(D[0], type(D[0]))