def insertion_sort(A) :
    n = len(A)						# 입력의 크기
    for i in range(1, n) :			# 외부 루프: 1, 2, ... n-1
        key = A[i]					# A[i]를 key에 저장
        j = i-1						# 항목 A[i-1]부터 검사
        while j>=0 and A[j] > key :	# 내부 루프
            A[j + 1] = A[j]			# 항목들을 오른쪽으로 한 칸씩 이동
            j = j - 1				# 위치를 왼쪽으로 이동
        A[j + 1] = key				# 항목 A[i]를 제 위치에 삽입
        printStep(A, i)

def printStep(arr, val) :					# 중간 과정 출력용 함수
    print("  Step %2d = " % val, end='')	# 현재 단계를 출력
    print(arr)							# 리스트의 내용을 출력

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)



