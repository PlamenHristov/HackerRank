#!/usr/bin/env python

def sumXORsubsets(entries):
    "Returns the sum of XOR(subset) for each subset of entries."
    mass_or = 0;
    for entry in entries: mass_or |= entry;
    return 2**(len(entries) - 1) * mass_or;
"""
For each bit, XOR(subset) is the parity of the number of subsets
for which that bit is 1.  Consider an entry e with specified bit of 1.
Then for each subset S of the rest of entries,
S and S+e differ over that bit. So our entry's inclusion/exclusion
divides the space of subsets into complements,
for which precisely one of each complement has that bit as 1.

Therefore if there is an entry e with specified bit of 1,
then precisely half the subsets have XORs with specified bit 1.
There are 2**N total subsets of a set of N elements,
so 2**(N-1) XORs of subsets have specified bit 1
if any entry has specified bit 1.
(If no entry has specified bit 1, all the XORs will leave 0 in that bit.)

The bitwise 'or' of all entries = all bits that appear in an entry.
For 1 bit in that or, 2**(N-1) XORs of subsets have that bit as 1.
So the sum of all the XORs is just ('or' of all entries) * 2**(N-1).
This is what sumXORsubsets does, allowing it to XOR 2**N subsets
in only O(N) time.
"""

#Note we could optimize for the modulus earlier,
#do modulo exponentiation, etc.
#For the given inputs, this seems unnecessary.

if __name__ == "__main__":
    modulus = 10**9 + 7;
    num_cases = int(input());
    for case in range(num_cases):
        count = int(input());
        array = [int(entry) for entry in input().split()];
        print(sumXORsubsets(array) % modulus);


import functools, operator as op, sys


MOD = 1000000007


bitfield = lambda n: [1 if d == '1' else 0 for d in bin(n)[2:][::-1]]


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        X = list(map(int, sys.stdin.readline().split()))

        x = functools.reduce(op.or_, X, 0)
        k = pow(2, N - 1, MOD)

        print(sum(k * (1 << i) for i, d in enumerate(bitfield(x)) if d) % MOD)