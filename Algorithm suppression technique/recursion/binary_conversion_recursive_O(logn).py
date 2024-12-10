# 자연수 2진수 변환(재귀)
import math
count = 0

def binary_digits(n) :			# 입력 양의 정수 n
    global count
    count += 1
    
    if n == 1 :			        # n이 1이면 길이는 1
        return 1
    else :				        # n이 1보다 크면
        return 1 + binary_digits(n//2)	# 1 + n//2의 길이

n = int(input("자연수 n을 입력하세요:"))
print(f"총 비트수 ({n}) = {binary_digits(n)}")
print(f"함수 호출 횟수: {count}")
print(f"log2({n})은 {math.log2(n):.4f}")



