import itertools
import sys


def g_func(input_set):
    res = 0
    for size, num in enumerate(input_set):
        for comb in itertools.combinations(input_set, size + 1):
            prod = 1
            for val in comb:
                prod *= val
            res += num * prod
    res %= (10 ** 9 + 7)
    return res


def main():
    N = int(input())
    input_set = list(map(int, sys.stdin.readline().split()))
    print(g_func(input_set))


if __name__ == '__main__':
    main()
    # 46
