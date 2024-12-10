import random

# 1부터 10까지의 수를 임의의 순서로 출력
numbers = [i for i in range(1, 11)]
random.shuffle(numbers)
print("임의의 순서로 출력된 1부터 10까지의 수:", numbers)

# 버블정렬로 내림차순으로 정렬
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("버블정렬로 내림차순으로 정렬된 1부터 10까지의 수:", numbers)

# ChatGPT:
# 질문:1부터 10까지의 수를 임의의 순서로 출력한 후에, 
#      버블정렬로 내림차순으로 정렬하는 파이썬 코드를 작성해줘 


