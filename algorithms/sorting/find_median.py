import sys


def quickSelect(A, k):
    if len(A) == 1: return A[0]

    p, L, R = A[0], [], []
    for i in A:
        if i < p: L.append(i)
        if i > p: R.append(i)

    if len(L) > k:
        return quickSelect(L, k)
    elif len(L) == k:
        return p
    else:
        return quickSelect(R, k - len(L) - 1)


import random


def partition(a, l, r):
    lp = l
    rp = lp
    while rp < r:
        if a[rp] < a[l]:
            lp += 1
            a[rp], a[lp] = a[lp], a[rp]
        rp += 1
    if a[l] > a[lp]:
        a[l], a[lp] = a[lp], a[l]
    return lp


def RSelect(a, n, order):
    i = 1
    pos = random.randrange(0, n)
    a[0], a[pos] = a[pos], a[0]

    pivot = a[0]
    a = [num for num in a if num < pivot] + [num for num in a if num >= pivot]
    for j in range(1, n):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i = i + 1;

    a[0], a[i - 1] = a[i - 1], a[0]

    if i == order:
        return pivot
    elif i > order:
        return RSelect(a[:i], len(a[:i]), order)
    elif i < order:
        return RSelect(a[i:], len(a[i:]), order - i)


def median_sort(ar):
    ar.sort()
    answer = ar[len(ar) // 2] if len(ar) % 2 == 0 else (ar[len(ar) // 2] + ar[len(ar) // 2 + 1]) / 2
    return int(answer)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))

    print(str(median_sort(ar)))
