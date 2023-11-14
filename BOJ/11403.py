# https://www.acmicpc.net/problem/11403
# 플로이드 워셜 알고리즘 사용
# 시간 복잡도는 3중 for문 O(n^3)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n)];
for i in range(n):
    graph[i] = list(map(int, input().rstrip().split(" ")))

for i in range(n):
    for j in range(n):
        if j==i:
            continue
        for k in range(n):
            if graph[j][k]==1:
                continue
            if graph[j][i]*graph[i][k]==1:
                graph[j][k] = 1

for i in range(n):
    print(*graph[i])
