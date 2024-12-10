# 날짜/시간과 관련된 기능을 가져옴
import datetime

# 현재 날짜/시간을 구함
now = datetime.datetime.now()

# 출력
print(now.year, " 년")
print(now.month, " 월")
print(now.day, " 일")
print(now.hour, " 시")
print(now.minute, " 분")
print(now.second, " 초")

# format() 출력
current_1 = "{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month, now.day,
    now.hour, now.minute, now.second
)
print(current_1)

# f-string(formatted string) : python 3.6 이후 가능
current_2 = f"{now.year}년 {now.month}월 {now.day}일 \
    {now.hour}시 {now.minute}분 {now.second}초"
print(current_2)


