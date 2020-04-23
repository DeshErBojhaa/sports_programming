from queue import SimpleQueue
class Solution:
    def calculate(self, s: str) -> int:
        ss = ''
        
        for c in s:
            if c in '()+-':
                ss += ' ' + c + ' '
            else:
                ss += c
        
        s = ss.split()
        
        num = []
        operator = []
        
        for c in s:
            if c.isnumeric():
                if operator and operator[-1] in '+-':
                    a = num.pop()
                    b = int(c)
                    op = operator.pop()
                    
                    if op == '+':
                        num.append(a + b)
                    else:
                        num.append(a - b)
                else:
                    num.append(int(c))
            else:
                if c == ')':
                    operator.pop()
                    if operator and operator[-1] in '-+':
                        if len(num) > 1:
                            a = num.pop()
                            b = num.pop()
                            op = operator.pop()
                            
                            if op == '+':
                                num.append(a + b)
                            else:
                                num.append(b - a)
                else:
                    operator.append(c)
                
        return num[-1]
