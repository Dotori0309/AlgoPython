# 제목: lambda 기초 - 익명 함수와 일반 함수의 차이

power_l = lambda x: x*x   # 람다식(람다함수)

def power_func(a): # 함수의 정의
    res = a * a
    return res

num = int(input("제곱을 구하고자 하는 숫자를 입력:"))

result = power_func(num) # 함수의 호출(실행)
result2 = power_l(num)

print(f"{num}의 제곱f은 {result}이다.")
print(f"{num}의 제곱l은 {result2}이다.")

