from pprint import pprint as pp


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        current_vertex = queue.pop(0)
        if current_vertex not in visited:
            visited.add(current_vertex)
            print(current_vertex)
            queue.extend(set(graph.get(current_vertex, [])) - visited)
    return visited


def bfs_path_orig(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_path_orig(graph, start, goal))
    except StopIteration:
        return None


def bfs_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        pp("Queue: ")
        pp(queue)
        pp("Vertex: {0}: {1}".format(vertex, path))
        pp("Coming next: {0}".format(set(graph.get(vertex, [])) - set(path)))
        print()
        visited.add(vertex)
        print("Visited: {0}".format(visited))
        for next_vertex in set(graph.get(vertex, [])) - set(path):
            if next_vertex == end:
                return path + [next_vertex]
            elif next_vertex not in visited:
                queue.append((next_vertex, path + [next_vertex]))

    return None


def build_matrix():
    buckets = []


def build_graph_normal():
    num_tests = int(input())
    for i in range(num_tests):

        num_ladders = int(input())
        ladders = []
        for _ in range(num_ladders):
            ladders.append(dict(map(int, input().split(' '))))

        num_snakes = int(input())
        snakes = []
        for _ in range(num_snakes):
            snakes.append(dict(map(int, input().split(' '))))

        adjacency_list = dict()
        for key in range(1, 101):
            adjacency_list.update({key: list(range(key + 1, key + 6))})

        for ladder in ladders:
            adjacency_list.update(ladder.items())

        for snake in snakes:
            adjacency_list.update({snake.key(): None})


def build_graph_test(input_ladders, input_snakes):
    adjacency_list = dict()
    for key in range(1, 101):
        adjacency_list.update({key: list(range(key + 1, key + 7))})

    adjacency_list.update(dict(input_ladders).items())

    for snake_key in dict(input_snakes).keys():
        adjacency_list.update({snake_key: [0]}.items())

    return adjacency_list

for t in range(int(input())):
    L,S=map(int,input().split(' '))
    ladders=[map(int,a.split(' ')) for a in input().split()]
    snakes=[map(int,a.split(' ')) for a in input().split()]
    ladders.extend(snakes)
    D={}
    for a,b in ladders:
        D[a]=b
    V=set() # visited squares
    S=set()
    S.add(1)
    moves=0
    while 100 not in S:
        moves+=1
        S2=set()
        for a in S:
            for d in range(1,6+1):
                n=a+d
                if n in D:
                    n=D[n]
                if n in V:
                    continue
                V.add(n)
                S2.add(n)
        S=S2
    print(moves)
    
def main():
    input_ladders = [(32, [62]),
                     (42, [68]),
                     (1, [9])]
    input_snakes = [(95, [13]),
                    (97, [25]),
                    (93, [37]),
                    (79, [27]),
                    (75, [19]),
                    (49, [47]),
                    (67, [1])]

    test_graph = {'A': set(['B', 'C']),
                  'B': set(['A', 'D', 'E']),
                  'C': set(['A', 'F']),
                  'D': set(['B']),
                  'E': set(['B', 'F']),
                  'F': set(['C', 'E'])}
    graph = build_graph_test(input_ladders, input_snakes)
    pp(graph)
    # pp(bfs_path(test_graph, 'A', 'F'))
    pp(bfs_path(graph, 1, 100))
    # pp(bfs(graph,1))

if __name__ == '__main__':
    main()
