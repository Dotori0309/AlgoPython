# 자연수의 2진수 변환

import math

def binary_digits(n) :		# 입력 양의 정수 n
    count = 1			    # 이진수의 최소 길이는 0
    while n > 1 :		    # n이 1보다 크면 더 나눌 수 있음
        count = count + 1	# count 증가
        n = n // 2		    # n의 몫을 구해 다시 n에 저장 (정수 나눗셈) 
    return count		    # count를 반환 

n = int(input("자연수 n을 입력하세요: "))
print(f"총 비트수 ({n}) = {binary_digits(n)}")
print(f"log2({n})은 {math.log2(n):.4f}")

