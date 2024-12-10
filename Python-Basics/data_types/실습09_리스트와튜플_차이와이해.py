# 제목: 리스트와 튜플의 차이와 이해 
def sunmoon():  # 함수의 정의
    return(11,12,13,14)   # 튜플로 결과 반환

aaa = sunmoon()
print(sunmoon(), type(sunmoon()))
print(aaa[0], type(aaa[0]))

[a,b] = [10, 20]   # 리스트 
(c,d) = (10,20)    # 튜플 
e = [100, 200, 300, 400]   # 리스트
f = 101, 201, 301, 401     # 튜플 
a,b = b,a

print('a:',a, 'type=',type(a))
print('b:',b, 'type=',type(b))
print('c:',c, 'type=',type(c))
print('d:',d, 'type=',type(d))
print('e:',e, 'type=',type(e))
print('f:',f, 'type=',type(f))

print(e[1])  # 리스트 요소 출력
print(f[1])  # 튜플 요소 출력


