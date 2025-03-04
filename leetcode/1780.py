# p = [3**i for i in range(15)]
# ass = set()
# for mask in range(2**14):
#     sm = 0
#     for i in range(15):
#         if mask & (1 << i):
#             sm += p[i]
#     ass.add(sm)
    
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # print()
        for i in range(14, -1, -1):
            now = 3 ** i
            if n and n >= now:
                n -= now
            # print(now, n)
        return not n
