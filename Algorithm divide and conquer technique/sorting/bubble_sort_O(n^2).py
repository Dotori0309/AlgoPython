def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] =array[j+1]
                array[j+1] = temp
            print(array)
            
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
bubble_sort(array)

# 참고: https://seanpark11.tistory.com/50


