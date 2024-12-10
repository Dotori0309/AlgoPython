def fib_dp_mem(n) :
    if( mem[n] == None ) :		# 풀리지 않은 경우-> 계산하고 저장
        if n < 2 :
            mem[n] = n			# 기반 상황: n<=1
        else: 					# 일반 상황: otherwise
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)	
    return mem[n]

def fib_dp_tab(n) :
    f = [None] * (n+1)			# 테이블을 만들고
    f[0] = 0					# 기반 상황 처리
    f[1] = 1					# 기반 상황 처리
    for i in range(2, n + 1):	# 상향식으로: 2, 3, ... n
        f[i] = f[i-1] + f[i-2]	# 부분 문제들을 해결하고 저장함
    return f[n]					# 결과 반환

n = 8
print('동적계획(  테이블화  ): Fibonacci(%d) = '%n, fib_dp_tab(n))
mem = [None] * (n+1)
print('동적계획(메모이제이션): Fibonacci(%d) = '%n, fib_dp_mem(n))


