import sys

if __name__ == '__main__':
    M, N, R = list(map(int, sys.stdin.readline().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for row in range(M)]
    for _ in range(R):
        matrix = list(zip(*matrix[::-1]))
    print(matrix)


def main():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    answer = [[2, 3, 4, 8],
              [1, 7, 11, 12],
              [5, 6, 10, 16],
              [9, 13, 14, 15]]

    rotated = [(13, 9, 5, 1),
               (14, 10, 6, 2),
               (15, 11, 7, 3),
               (16, 12, 8, 4)]
