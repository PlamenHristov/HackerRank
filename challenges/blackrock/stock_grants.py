import sys
def test():

    N = 12
    rating = [6, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
    min = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]
    res = 53
    res_list = [7, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7]
N = int(sys.stdin.readline())
rating = list(map(int, sys.stdin.readline().split()))
min_num_shares = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1):
    if rating[i + 1] > rating[i]:
        min_num_shares[i + 1] = min_num_shares[i] + 1

for i in reversed(range(N - 1)):
    if rating[i] > rating[i + 1] and min_num_shares[i] <= min_num_shares[i + 1]:
        min_num_shares[i] = min_num_shares[i + 1] + 1
print(min_num_shares)
print(sum(min_num_shares))
