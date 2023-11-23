from collections import deque
import sys
input = sys.stdin.readline

print("노드의 개수는?",end="")
n = int(input())

tmp_n = n

print("간선의 개수는?",end="")
edge_cnt = int(input())

matrix = [[0]*(n+1) for i in range(n+1)]

print("간선의 연결 관계를 입력하시오.")

Graph_nodes = [i for i in range(1,n+1)]

D = {}

σ = [0]*(n+1) ## index 1부터 시작하도록 n+1곱함.

d = [0]*(n+1)

P = [[]for i in range(n+1)]

for i in range(edge_cnt):
    a,b = map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

linked_node_to_me = [[] for i in range(n+1)]

for i in range(1,len(linked_node_to_me)):
    for j in range(1,len(matrix[i])):
        if matrix[i][j]:
            linked_node_to_me[i].append(j)

for n in Graph_nodes:
    D[n] = 0

for n in Graph_nodes:
    for m in Graph_nodes:
        if n == m:
            continue

        P[m] = []
        σ[m] = 0
        d[m] = -1
    
    P[n] = []           
    σ[n] = 1
    d[n] = 0

    stack_S = []

    Waiting_Q = deque()

    Waiting_Q.append(n)

    while Waiting_Q:
        o = Waiting_Q.popleft()
        stack_S.append(o)

        for p in linked_node_to_me[o]:
            if d[p] < 0:
                Waiting_Q.append(p)
                d[p] = d[o] + 1
            if d[p] == d[o] + 1:
                σ[p] += σ[o]
                P[p].append(o)
    
    δ = [0]*(tmp_n+1)

    while stack_S:
        q = stack_S.pop()

        for r in P[q]:
            δ[r] += round((σ[r]/σ[q])*(1+δ[q]),2)

        if q != n:      
            D[q] += δ[q]

for ki in D.keys():
    tmp = round(D[ki],4)
    D[ki] = tmp

print(D)
