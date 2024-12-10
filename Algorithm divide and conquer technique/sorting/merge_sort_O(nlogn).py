def merge_sort(A, left, right) :	    # A[left..right]를 오름차순으로 정렬
	if left<right :					    # 항목이 2개 이상인 경우
		mid = (left + right) // 2		# 리스트의 균등 분할
		merge_sort(A, left, mid)		# 부분 리스트 정렬
		merge_sort(A, mid + 1, right)	# 부분 리스트 정렬
		merge(A, left, mid, right)	    # 병합
	# else: 항목이 1개 인 경우. 자동으로 정복되었음(하나이므로)

def merge(A, left, mid, right) :
    k = left					# 병합을 위한 임시 리스트의 인덱스
    i = left					# 왼쪽 리스트의 인덱스
    j = mid + 1				# 오른쪽 리스트의 인덱스
    while i<=mid and j<=right :
        if A[i] <= A[j] :		# 기본 연산
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :				# 한쪽에 남아 있는 레코드의 일괄 복사
        sorted[k:k+right-j+1] = A[j:right+1]	# 리스트의 슬라이싱 이용
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]		# 리스트의 슬라이싱 이용

    A[left:right+1] = sorted[left:right+1]		# sorted를 A에 다시 복사

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]	# 입력 리스트
sorted = [0] * len(data)			# 길이가 len(data)인 임시 리스트를
print("Original  : ", data)			# 만들고 모든 항목을 0으로 초기화
merge_sort(data, 0, len(data)-1)	# 병합 정렬
print("MergeSort : ", data)


