def min_coins_greedy( coins, V ): 
    count = []					# 각 동전의 개수 저장
    for i in range(len(coins)) :
        cnt = V // coins[i]		# 현재 액면가의 최대 사용 가능 개수
        count.append(cnt)
        V -= cnt * coins[i]		# 남은 거스름돈 계산
    return count


coins = [500 , 100 , 50 , 10 , 5 , 1] 
V = 580
print("잔돈 액수 = ", V)
print("동전 종류 = ", coins)
print("동전 개수 = ", min_coins_greedy(coins, V ))

