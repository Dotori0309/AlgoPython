array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:  # 길이가 1까지 도달한 경우 고대로 리턴
        return array

    pivot = array[0]  # 이 경우, 첫 원소를 피벗으로 삼음
    tail = array[1:]  # 피벗 제외 배열 슬라이싱

    left_side = [x for x in tail if x <= pivot]  # 피벗보다 작거나 같은 원소만 모은 배열 
    right_side = [x for x in tail if x > pivot]  # 피벗보다 큰 원소만 모은 배열

    # 피벗의 자리는 결정되었고, 피벗 기준 왼쪽 배열과 오른쪽 배열에 대해 재귀 수행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


