def sale(securities, M, K):
    sorted_sec = sorted(securities, key=lambda x: x[0] * x[1], reverse=True)
    res = 0
    for i in range(M):
        if K > 0:
            x, _ = sorted_sec[i]
            y = 1
        else:
            x, y = sorted_sec[i]
        K -= 1
        res += x * y

    print(res)


#     N, M, K = list(map(int, input().split()))
#
#     securities = []
#     for _ in range(N):
#         securities.append(tuple(map(int, input().split())))
#         print(securities)


def test():
    N, M, K = 3, 2, 1
    price = [(5, 10), (6, 60), (8, 40)]
    sale(price, M, K)
    # 1116/100


if __name__ == '__main__':
    test()
