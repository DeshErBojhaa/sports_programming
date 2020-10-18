# 393. UTF-8 Validation
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, N = 0, len(data)
        
        while i < N:
            num = data[i]
            i += 1
            if num > 247:
                # print('1 Returning False')
                return False
            start = bin(num)[2:]
            if len(start) > 8:
                # print('2 Returning False')
                return False
            if len(start) < 8:
                start = ''.join(['0'] * (8 - len(start))) + start
            
            first_zero_index = start.find('0')
            if first_zero_index == 0:
                continue
            if first_zero_index < 2:
                # print('3 Returning False', num, first_zero_index)
                return False
            
            # print(i, data[i], i+first_zero_index-1)
            lim = i+first_zero_index-1
            while i < lim:
                if i == N or data[i] > 255 or data[i] < 128:
                    # print('4 Returning False', data[i], first_zero_index, i)
                    return False
                i += 1
            # print('Out Last Loop', i, data[i])
        return True

