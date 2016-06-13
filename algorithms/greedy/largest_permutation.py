import sys


def largest_permutation(N, K, A):
    if K >= N - 1:
        print(*sorted(A, reverse=True), sep=' ')

    else:
        max_num = sys.stdin.readline()

        for i in range(len(A))

        print(*A, sep=' ')


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
