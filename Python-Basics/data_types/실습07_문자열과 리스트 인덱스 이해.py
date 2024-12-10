#제목: 문자열과 인덱스의 이해

univ="선문대학교"
text="동해물과 백두산이 마르고 닳도록"
line=text.split(" ")

# 문자열
print(univ, "type: ",type(univ))
print(univ[0], "type: ",type(univ[0]))
print(univ[0:3], "type: ",type(univ[0:3]))
print(univ[-1], "type: ",type(univ[-1]))

print(line[0], "type: ", type(line[0]))

# 리스트
print(line, "type: ", type(line))

