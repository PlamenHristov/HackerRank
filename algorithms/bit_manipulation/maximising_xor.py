#!/usr/bin/python3
def maxXor(l, r):
    x = l ^ r
    if x == 0:
        return 0
    ret = 1
    print(x)
    while ret <= x:
        print(ret)
        ret <<= 1
    return ret - 1


def maxXorBrute(l, r):
    return max(A ^ B for A in range(l, r + 1) for B in range(l, r + 1))


if __name__ == '__main__':
    # l = int(input())
    # r = int(input())
    print(maxXor(10, 15))
