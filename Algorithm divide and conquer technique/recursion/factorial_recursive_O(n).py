# 팩토리얼 계산 문제
count_r = 0
count_i = 0

def factorial(n) :			# 순환적으로 구현한 factorial 함수
    global count_r
    count_r += 1
    if n == 0 :			    # 종료 조건
        return 1			# 순환을 멈추는 부분
    else :
        return n * factorial(n - 1)	# 자기 자신을 순환적으로 호출 

def factorial_iter(n) :		 # 반복 구조로 구현한 Factorial 함수
    global count_i
    count_i += 1
    result = 1	
    for k in range(n, 0, -1) :	# k: n, n-1, ..., 2, 1
        result = result * k	    # 기본 연산
    return result

n = int(input("정수 n을 입력하세요:"))

print(f"순환 Factorial({n})={factorial(n)} 호출 횟수: {count_r}")
print(f"반복 Factorial({n})={factorial_iter(n)} 호출 횟수: {count_i}")


