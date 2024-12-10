# 입력
number = input("정수 입력:")

# 마지막 자리 숫자를 추출
last_character = number[-1]
print(last_character)

# 숫자로 변환
last_number = int(last_character)

# 짝수 홀수 확인: 나머지 연산자(%) 
if last_number % 2 == 0:
    print("{}는짝수 입니다".format(number))
else:
    print(f"{number} 홀수 입니다.")


