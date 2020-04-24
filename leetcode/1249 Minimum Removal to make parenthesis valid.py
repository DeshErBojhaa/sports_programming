class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sl = list(s)
        balance = 0
        for i, v in enumerate(sl):
            if v == '(':
                balance += 1
            elif v == ')':
                balance -= 1
                if balance < 0:
                    sl[i] = ''
                    balance += 1
        
        for i in range(len(sl)-1, -1, -1):
            if not balance:
                break
            if sl[i] == '(':
                sl[i] = ''
                balance -= 1
        return ''.join(sl)
