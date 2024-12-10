# Fibonacci (순환): O(2^n)
def fib(n) :
    if n == 0 :
        return 0		# 정복: 0번째 달
    elif n == 1 :
        return 1		# 정복: 1번째 달
    else : 
        return fib(n - 1) + fib(n - 2)	

# Fibonacci (반복): O(n)
def fib_iter(n) :
	if (n < 2): return n
	last = 0
	current = 1
	for i in range(2, n+1) :
		tmp = current
		current += last
		last = tmp
	return current

# Fibonacci (축소 정복 기법의 행렬 거듭제곱 이용)
def fib_mat(n):
    if n < 2:
        return n
    mat = [[1,1], [1,0]]
    result = powerMat(mat, n)
    return result[0][1]

def powerMat(mat, n):
    if n == 1:
        return mat
    else:
        half_n = powerMat(mat, n // 2)
        if n % 2 == 0:
            return multiplyMat(half_n, half_n)
        else:
            return multiplyMat(multiplyMat(half_n, half_n), mat)   
        
def multiplyMat(mat1, mat2):
    result = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

# 피보나치 수열 순환, 반복, 행렬 함수 호출
print('Fibonacci 순환(5) = ', fib(5))
print('Fibonacci 반복(5) = ', fib_iter(5))
print('Fibonacci 행렬(5) = ', fib_mat(5))

for i in range (11) :
    print('fib 순환(%d)='%i, fib(i))
    print('fib 반복(%d)='%i, fib_iter(i))
    print('fib 행렬(%d)='%i, fib_mat(i))
    
    
    