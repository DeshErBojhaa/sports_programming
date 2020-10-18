# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        cur_num, cur_str = 0, ''
        stack = []
        
        for i in s:
            if i == '[':
                stack.extend([cur_str, cur_num])
                cur_num = 0
                cur_str = ''
            if i == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str =  prev_str + cur_str * num
            if i.isalpha():
                cur_str += i
            if i.isdigit():
                cur_num = cur_num * 10 + int(i)
        
        return cur_str

"2[abc]3[cd]ef"
"1[a12[r3[er]rr]]"
