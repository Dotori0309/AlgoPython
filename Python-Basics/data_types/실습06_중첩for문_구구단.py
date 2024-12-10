# 입력한 n단 까지 구구단 출력
n =int(input("n을 입력하세요")) 

# 첫번째 for문 i
for i in range(1, 10):
    # 두번째 for문 i
    for j in range(2, n+1):
        # f-string으로 구구단 문자열
        gugudan = f"{j} x {i} = {j*i}"
        print(gugudan, end="\t")
    print()

