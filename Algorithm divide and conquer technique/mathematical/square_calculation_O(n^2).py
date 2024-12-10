# 정수 n의 제곱 계산 함수
def compute_square_A(n) :	#  알고리즘 A 사용
    count = 0
    count += 1
    return n*n, count		        # 기본 연산: n*n

def compute_square_B(n) :	# 알고리즘 B 사용
    sum = 0
    count = 0
    for i in range(n) :	    # i : 0, 1, ... n-1
        sum = sum + n	    # 기본 연산
        count += 1
    return sum, count

def compute_square_C(n) :	#  알고리즘 C 사용
    sum = 0
    count = 0
    for i in range(n) :	    # i : 0, 1, ... n-1
        for j in range(n) :	# j : 0, 1, ... n-1
            sum = sum + 1	# 기본 연산
            count += 1
    return sum, count	

n = int(input("정수 n을 입력하세요: "))

print("알고리즘 A 결과:%d \
    횟수:%d" % (compute_square_A(n)[0], compute_square_A(n)[1]))
print("알고리즘 B 결과:{:d} \
    횟수:{:d}".format(compute_square_B(n)[0], compute_square_B(n)[1]))
print(f"알고리즘 C 결과:{compute_square_C(n)[0]} \
    횟수:{compute_square_C(n)[1]}")



