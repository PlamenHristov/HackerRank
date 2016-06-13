from collections import defaultdict
import heapq


def prim(G, S):
    visited = set()
    queue = [(0, S)]
    total_cost = 0
    while queue:
        cost, vertex = heapq.heappop(queue)
        if vertex not in visited:
            total_cost += cost
            visited.add(vertex)
            # We have reached an MST
            if len(G.keys()) == len(visited):
                return total_cost

            for next_cost, next_vertex in G[vertex]:
                heapq.heappush(queue, (next_cost, next_vertex))


def build_graph(M):
    G = defaultdict(set)
    for _ in range(M):
        e = [int(i) for i in input().split()]
        G[e[0]].add((e[2], e[1]))
        G[e[1]].add((e[2], e[0]))
    return G


def main():
    N, M = [int(i) for i in input().split()]
    G = build_graph(M)
    S = int(input())

    print(prim(G, S))


if __name__ == "__main__":
    main()
