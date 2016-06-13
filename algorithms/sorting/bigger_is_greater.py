def next_perm(s):
    # Find the longest non-increasing suffix
    i = len(s) - 1
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1

    if i <= 0:
        return None

    # Find successor pivot
    j = len(s) - 1
    while (s[j] <= s[i - 1]):
        j -= 1

    s[i - 1], s[j] = s[j], s[i - 1]

    # Reverse the suffix
    s[i:] = s[len(s) - 1: i - 1: -1]

    return ''.join(s)


def main():
    s = list('ab')
    print(next_perm(s))

    s = list('bb')
    print(next_perm(s))

    s = list('hefg')
    print(next_perm(s))

    s = list('dhck')
    print(next_perm(s))

    s = list('dkhc')
    print(next_perm(s))



if __name__ == '__main__':
    main()
