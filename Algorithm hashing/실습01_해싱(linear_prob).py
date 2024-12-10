M = 13					# 테이블의 크기
table = [None]*M			# 테이블 만들기: None으로 초기화
def hashFn(key) :		# 해시 함수
    return key % M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
    # while count>0 and (table[id] != None) :
        id = (id + 1 + M) % M		# 다음 위치로 이동
        count -= 1				# 검사할 남은 위치의 수
    if count > 0 :
        table[id] = key			# 해당 슬롯에 항목 저장
    return

def lp_search(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None :  # 찾는 항목이 테이블에 없음
            return None
        #if table[id] == key : 
        if table[id] != -1 and table[id] == key : 
            return table[id]    # 찾는 항목이 테이블에 있음
        id = (id + 1 + M) % M   # 없으면 다음 위치 검사
        count -= 1
    return None

def lp_delete(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None : return
        if table[id] != -1 and table[id] == key : 
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

print("   최초:", table )
lp_insert(45);  print( "45 삽입:", table )
lp_insert(27);  print( "27 삽입:", table )
lp_insert(88);  print( "88 삽입:", table )
lp_insert(9);   print( " 9 삽입:", table )
lp_insert(71);  print("71 삽입:", table )
lp_insert(60);  print("60 삽입:", table )
lp_insert(46);  print("46 삽입:", table )
lp_insert(38);  print("38 삽입:", table )
lp_insert(24);  print("24 삽입:", table )
lp_delete(60);  print("60 삭제:", table )
print("46 탐색:", lp_search(46) )

def hashFn(key) :
	sum = 0
	for c in key :				# 문자열의 모든 문자에 대해
		sum = sum +  ord(c)		# 그 문자의 아스키 코드 값을 sum에 더함
	return sum % M


