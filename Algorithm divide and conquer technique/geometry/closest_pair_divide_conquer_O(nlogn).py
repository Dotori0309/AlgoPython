import math				    # math 모듈 포함. 제곱근(sqrt) 함수 사용을 위해

def distance(p1, p2):		# Euclidean 거리 계산 함수
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(p):
    n = len(p)              			# 점의 전체 개수
    mindist = float("inf")  			# 최근접 거리 초기화(무한대)
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])	# 유클리드 거리 계산
            if dist < mindist:
                mindist = dist
    return mindist

def strip_closest(P, d): 
    n = len(P)                  # 리스트내의 점의 수
    d_min = d
    P.sort(key = lambda point: point[1])  # y축을 따라 정렬

    for i in range(n):          # y가 최소인 점부터 순서대로
        j = i + 1
        # P[i].y와 P[j].y의 차이가 d_min 이내일 때 까지만 처리
        while j < n and (P[j][1] - P[i][1]) < d_min: 
            dij = dist(P[i], P[j]) 
            if dij < d_min :
                d_min = dij
            j += 1
    return d_min                # d_min 반환

def closest_pair_dist(P, n): 
    if n <= 3:			            # 점이 3개 이하이면, brute force로 바로 계산
        return closest_pair(P)  	# 억지기법 알고리즘(알고리즘 3.4) 

    mid = n // 2			# 중앙점을 찾음. P는 현재 x로 정렬되어 있음
    mid_x = P[mid][0] 		# 중앙점의 x좌표 

    dl = closest_pair_dist(P[:mid], mid)	# Pl에서 dl 계산
    dr = closest_pair_dist(P[mid:], n-mid)	# Pr에서 dr 계산
    d = min(dl, dr)		# d는 둘 중에서 더 짧은 거리

    Pm = []				# 중앙에서 x좌표가 d이내인 점들의 집합 Pm을 만듦
    for i in range(n):	# Pm도 x에 대해 정렬되어 있음
        if abs(P[i][0] - mid_x) < d:  
            Pm.append(P[i]) 

    ds = strip_closest(Pm, d)	# Pm내에서 d보다 작은 최근접쌍 거리 찾기
    return min(d, ds)

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p.sort(key = lambda point: point[0])    # 전처리: 점들을 x순으로 정렬
print("가장 가까운 두 점의 거리", closest_pair_dist(p, len(p))) 


