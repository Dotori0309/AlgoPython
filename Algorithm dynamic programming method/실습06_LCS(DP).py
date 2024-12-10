def lcs_dc(X, Y, m, n): 
    if m == 0 or n == 0: 			# base case 
        return 0 
    elif X[m-1] == Y[n-1]: 		# case 1: x_m == y_n
        return 1 + lcs_dc(X, Y, m-1, n-1) 
    else: 						# case 2
        return max(lcs_dc(X, Y, m, n-1), lcs_dc(X, Y, m-1, n)) 

def lcs_dp(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)] 	# 테이블 생성

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :	# base case: 하나의 길이라도 0이면
                L[i][j] = 0			# LCS --> 0
            elif X[i-1] == Y[j-1]:	# 마지막 글자가 같으면
                L[i][j] = L[i-1][j-1]+1
            else:					# 마지막 글자가 다르면
                L[i][j] = max(L[i-1][j], L[i][j-1])

    for i in range(m+1):
        print(L[i])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n] 

def lcs_dp_traceback(X, Y, L):
    lcs = ""													# ①
    i = len(X)													# ②
    j = len(Y)													# ② 
    while i > 0 and j > 0:
        v = L[i][j] 
        if v > L[i][j-1] and v > L[i-1][j]  and v > L[i-1][j-1]:# ③
            i -= 1
            j -= 1
            lcs = X[i] + lcs

        elif v == L[i][j-1] and v > L[i-1][j]: j -= 1			# ④
        else : i -= 1											# ⑤
    return lcs

X = "GAME OVER"
Y = "HELLO WORLD"
print("X = ", X)
print("Y = ", Y)
print("LCS(분할 정복)", lcs_dc(X , Y, len(X), len(Y)))
print("LCS(동적 계획)", lcs_dp(X , Y) )

