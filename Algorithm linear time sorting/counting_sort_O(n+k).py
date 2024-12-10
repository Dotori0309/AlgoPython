def counting_sort(A): 
    output = [0] * len(A)				# 정렬 결과저장용 임시 리스트
    count  = [0] * MAX_VAL      		# 각 숫자의 빈도를 저장

    for i in A:                 		# 각 숫자별 빈도를 계산
        count[i] += 1

    for i in range(MAX_VAL):    		# count[i]가 출력 배열에서  
        count[i] += count[i-1]  		# 해당 숫자의 위치가 되도록 수정

    for i in range(len(A)):     		# 모든 입력항목 A[i]에 대해
        output[count[A[i]]-1] = A[i] 	# 해당 위치(count[A[i]]-1)에 저장
        count[A[i]] -= 1				# 킷값 A[i]의 위치를 하나 줄임

    for i in range(len(A)):     		# 정렬 결과를 원래 배열에 복사
        A[i] = output[i] 

MAX_VAL = 10
data = [ 1, 4, 1, 2, 7, 5, 2 ]
print("Original  : ", data)
counting_sort(data)             # 카운팅 정렬
print("Counting  : ", data)


