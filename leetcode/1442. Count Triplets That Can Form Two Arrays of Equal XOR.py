# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, xor = 0, 0
        dic = {0:[1, 0]}
        
        for i, v in enumerate(arr):
            xor ^= v
            prev_occurrences, indices_sum = dic.get(xor, [0, 0])
            res += i * prev_occurrences - indices_sum
            dic[xor] = [prev_occurrences + 1, indices_sum + i + 1]
        
        return res

# See lee's explanation if confused.
