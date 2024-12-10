# 제목 : BMI지수로 비만도 판별하기

height = float(input("키를 m로 입력하세요:"))
weight = float(input("몸무게를 kg로 입력하세요:"))

# 함수 정의 - BMI 계산
def calcBMI(height, weight):
    bmi = weight / (height*height) 
    return bmi

# 함수 정의 - 비만도 판별
def checkBMI(bmi):
    if bmi > 30:
        print(f"당신의 BMI는 {bmi:.1f}이고, 비만입니다.")
    elif bmi > 25:
        print(f"당신의 BMI는 {bmi:.1f}이고, 정상입니다.")
    elif bmi > 18:
        print(f"당신의 BMI는 {bmi:.1f}이고, 저체중입니다.")    
        
# 함수 호출(실행)
result = calcBMI(height,weight)
checkBMI(result)     
 
 
 