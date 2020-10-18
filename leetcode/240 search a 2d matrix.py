class Solution:
    def searchMatrix(self, m, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not m:
            return False
        
        C, j = len(m[0]), -1
        if not C:
            return False
        for row in m:
            while (j + C)>=0 and row[j] > target:
                j -= 1
            if (j + C)>=0 and row[j] == target:
                return True
        return False
