# 하노이의탑 문제
count = 0

def hanoi_tower(n, fr, tmp, to) :		        # Hanoi Tower 순환 함수
    global count
    count += 1
    if (n == 1) :				                # 종료 조건
        print("원판 1: %s --> %s" % (fr, to))	# 가장 작은 원판을 옮김
    else :
        hanoi_tower(n - 1, fr, to, tmp)		    # n-1개를  to를 이용해 tmp로
        print("원판 %d: %s --> %s" % (n,fr,to))	# 하나의 원판을 옮김
        hanoi_tower(n - 1, tmp, fr, to)		    # n-1개를  fr을 이용해 to로

n = int(input("원반의 갯수 n(자연수)를 입력하세요:"))
hanoi_tower(n, 'A', 'B', 'C')

print(f"함수 호출 횟수: {count}")


