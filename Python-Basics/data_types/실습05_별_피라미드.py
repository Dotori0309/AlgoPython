n = int(input("피라미드 층수를 입력하시오: "))

for i in range(0, n+1):    
    for j in range(0, i):
        print("*", end="")
    print()
    
print("-----------------")

for i in range(0, n):    
    for k in range(1, n-i):
        print(" ", end="")
    for j in range(0, i*2+1):
        print("*", end="")
    print()




