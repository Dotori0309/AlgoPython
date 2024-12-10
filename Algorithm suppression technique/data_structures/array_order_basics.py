# # generator 리스트 내포(list comprehension)
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nums = [ i for i in range(1,10)]
my_list = [x for x in nums if x % 2 == 0] 
print(my_list)

# # 별표(*): 언패킹 연습
# (a1, b1, *c1) = numbers
# (*c2, a2, b2) =  numbers
# (a3, *c3, b3) = numbers

# print(*c1)
# print(*c2)
# print(*c3)
# print(c1, type(c1))
# print(c2, type(c2))
# print(c3, type(c3))

# 순열 연습
# from itertools import permutations
# n = int(input())    

# for i in permutations(range(1,n),n-1):
#     # num_list = i
#     num_list = [i]
#     # num_list = [*i]
    
#     print(num_list, type(num_list))
    
    