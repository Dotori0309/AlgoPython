import copy							# 리스트의 깊은 복사를 위해 사용
def shortest_path_floyd(vertex, W):	# Floyd의 최단경로탐색 함수.
    vsize = len(vertex)       		# 정점의 개수
    D = copy.deepcopy(W)				# 깊은 복사

    for k in range(vsize) :			# 정점 k를 추가할 때
        for i in range(vsize) :
            for j in range(vsize) :	# 모든 D[i][j] 갱신
                if (D[i][k] + D[k][j] < D[i][j]) :
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)					# 현재 D 행렬 출력 

def printD(D):	# 현재의 최단거리 행렬 D를 화면에 출력하는 함수
    vsize = len(D)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (D[i][j] == INF) : print(" INF ", end='')
            else : print("%4d "%D[i][j], end='')
        print("")

INF = 9999
vertex = [  'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [  [   0,   7, INF, INF,   3,  10, INF ],
            [   7,   0,   4,  10,   2,   6, INF ],
            [ INF,   4,   0,   2, INF, INF, INF ],
            [ INF,  10,   2,   0,  11,   9,   4 ],
            [   3,   2, INF,  11,   0,  13,   5 ],
            [  10,   6, INF,   9,  13,   0, INF ],
            [ INF, INF, INF,   4,   5, INF,   0 ]]
print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)


