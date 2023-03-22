import sys
import heapq

input = sys.stdin.readline
N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1e9
v1,v2 = map(int,input().split())
visited=[INF for _ in range(N+1)]


def dijkstra(start):
    distance = [INF]*(N+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

org_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = org_distance[v1]+v1_distance[v2]+v2_distance[N]
v2_path = org_distance[v2]+v2_distance[v1]+v1_distance[N]

result=(min(v1_path, v2_path))
print(result if result<INF else -1)