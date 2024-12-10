def shortest_path_dijkstra(vtx, adj, start) :
    vsize = len(vtx)					# 정점 수
    dist = list(adj[start])			# dist 배열 생성 및 초기화
    dist[start] = 0					# 시작정점의 거리 0
    path = [start] * vsize			# path 배열 생성 및 초기화
    found= [False] * vsize			# found 배열 생성 및 초기화
    found[start] = True				# 시작정점: 이미 찾아짐

    for i in range(vsize) :
        print("Step%2d: "%(i+1),dist) 	# 단계별 dist[] 출력용 
        u = getMinVertex(dist, found)	# 알고리즘 8.5 사용
        found[u] = True				# u는 이제 찾아짐

        for w in range(vsize) :		# 모든 정점에 대해
            if not found[w] :			# 아직 찾아지지 않았으면
                if dist[u] + adj[u][w] < dist[w] :	# 갱신 조건 검사
                    dist[w] = dist[u] + adj[u][w]	# dist 갱신
                    path[w] = u		# 이전 정점 갱신

    return path						# 찾아진 최단 경로 반환

def getMinVertex(dist, selected) :
    minv = -1	
    mindist = INF
    for v in range(len(dist)) :					# 모든 정점들에 대해
        if not selected[v] and dist[v]<mindist :	# 선택 안 되었고  
            mindist = dist[v]						# 가중치가 작으면
            minv = v								# minv 갱신
    return minv					# 최소 가중치의 정점 반환

INF = 9999
vertex = [  'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [  [    0,   7, INF, INF,   3,  10, INF ],
            [    7,   0,   4,  10,   2,   6, INF ],
            [  INF,   4,   0,   2, INF, INF, INF ],
            [  INF,  10,   2,   0,  11,   9,   4 ],
            [    3,   2, INF,  11,   0,  13,   5 ],
            [   10,   6, INF,   9,  13,   0, INF ],
            [  INF, INF, INF,   4,   5, INF,   0 ]]

print("Shortest Path By Dijkstra Algorithm")
start = 0	# 시작 정점은 0번(A)
path = shortest_path_dijkstra(vertex, weight, start)

# 최종 경로를 출력하기 위한 코드
for end in range(len(vertex)) :
    if end != start :
        print("[최단경로: %s->%s] %s" %
				(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start) :
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])


