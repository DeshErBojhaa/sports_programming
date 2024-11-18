class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        arr = [0] * N
        
        if k == 0:
            return arr
        
        for i in range(N):
            if k > 0:
                sm = 0
                for j in range(i + 1, i+k +1):
                    sm += code[j%N]
                arr[i] = sm
            else:
                sm = 0
                for j in range(i-1, i + k-1, -1):
                    print(i, j)
                    sm += code[j%N]
                arr[i] = sm
        return arr
