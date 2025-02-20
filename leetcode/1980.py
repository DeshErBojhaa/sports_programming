class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(int(x, 2) for x in nums)
        for i in range(2 ** (len(nums[0])+1)):
            if i not in s:
                xx = bin(i)[2:]
                diff = ''
                if len(xx) < len(nums[0]):
                    diff = ''.join(['0'] * (len(nums[0]) - len(xx)))
                return diff + xx
                
