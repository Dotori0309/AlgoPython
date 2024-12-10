# 변수 선언
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환하고자 하는 금액은? "))

# 몫(//)과 나머지(%) 연산자
c500 = money // 500
money %= 500 # money = money % 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n500원 짜리: %d 개" % c500)
print("\n100원 짜리: %d 개" % c100)
print("\n 50원 짜리: %d 개" % c50)
print("\n 10원 짜리: %d 개" % c10)
print("\n      잔돈: %d 개" % money)

