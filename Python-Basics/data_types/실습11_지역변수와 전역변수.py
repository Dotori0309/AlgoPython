# 제목 : 함수의 이해 - 지역변수와 전역변수 
coffee = 3

# 함수의 정의
def coffeeMachine(coffee):
    print("coffeeMachine")
    print("#1. 뜨거운 물을 준비한다.")
    print("#2. 종이컵을 준비한다.")

    if coffee == 1:
        print("#3. 보통 커피를 탄다.")
    elif coffee == 2:
        print("#3. 설탕 커피를 탄다.")
    elif coffee == 3:
        print("#3. 블랙 커피를 탄다.")
    else:
        print("#3. 아무거나 탄다.")

    print("#4. 물을 탄다.")
    print("#5. 스푼으로 젓는다.")

# 함수의 정의    
def testPrint():
    print("testPrint")
    print(coffee)  
    
# main부분
if __name__ == "__main__":        
    a = int(input("커피 선택(1: 보통, 2: 설탕, 3: 블랙)"))
    coffeeMachine(a)    
    testPrint()

    print()
    print("손님 커피 드세요")
    
    
    