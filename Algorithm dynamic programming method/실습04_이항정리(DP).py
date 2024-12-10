def bino_coef_dc(n , k): 
    if k==0 or k ==n : 
        return 1
    return bino_coef_dc(n-1 , k-1) + bino_coef_dc(n-1 , k) 

def bino_coef_dp(n, k): 
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)] 

    for i in range(n+1):				# bottom-up 방향으로 진행: i:0~n
        for j in range(min(i, k)+1):	# j: 0~n
            if j == 0 or j == i:		# 정의에 의해 (base case)
                C[i][j] = 1			# C(n,0) = C(n,n) = 1 --> 저장
            else:					# 보다 큰 부분문제 해결 --> 저장
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
    return C[n][k]					# 최종 결과

print("[Divide and Conquer ] C(6,3) = ", bino_coef_dc(6, 3))	# 분할 정복
print("[Dynamic Programming] C(6,3) = ", bino_coef_dp(6, 3))	# 동적 계획

