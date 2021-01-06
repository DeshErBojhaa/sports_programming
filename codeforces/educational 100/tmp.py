from collections import Counter
# Python3 program to print n-th permutation

MAX_FACT = 31
fact = [None] * (MAX_FACT)

def precomputeFactorials():
    fact[0] = 1
    for i in range(1, MAX_FACT):
            fact[i] = fact[i - 1] * i

def nPermute(string, n):
    precomputeFactorials()

    length = len(string)
    freq = Counter(string)
    freq = [freq['H'], freq['V']]

    out = [None] * length

    Sum, k = 0, 0

    while Sum != n:
        Sum = 0
        for i in range(2):
            if freq[i] == 0:
                continue

            # Remove character
            freq[i] -= 1

            xsum = fact[length - 1 - k]
            for j in range(2):
                xsum = xsum // fact[freq[j]]
            Sum += xsum

            if Sum >= n:
                out[k] = ('H' if i == 0 else 'V')
                n -= Sum - xsum
                k += 1
                break

            if Sum < n:
                freq[i] += 1

    i = 1
    while k < length and i >= 0:
        if freq[i]:
            out[k] = 'V'
            freq[i] -= 1
            i += 1
            k += 1

        i -= 1

    print(''.join(out[:k]))

# Driver Code
if __name__ == "__main__":

    n = 3
    string = "HHHHVV"

    nPermute(string, n)

# This code is contributed by Rituraj Jain
