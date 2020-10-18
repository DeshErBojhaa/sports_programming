# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

# 1533. Find the Index of the Large Integer
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        st, ed = 0, reader.length() - 1
        while st < ed:
            tmp_ed = ed
            if (ed - st + 1) & 1 and (ed - st) > 0:
                tmp_ed = ed - 1
                odd = True
            ls, le = st, (st + tmp_ed)//2
            rs, re = ((st+tmp_ed)//2)+1, tmp_ed

            cmp = reader.compareSub(ls, le, rs, re)
            if cmp == 1:
                ed = le
            elif cmp == -1:
                st = rs
            else:
                return ed
                
        return st


        
