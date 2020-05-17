# 640. Solve the Equation
class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs, rhs = equation.split('=')
        
        def reduce_x(xs):
            val = 0
            sign = 1
            for i, v in enumerate(xs):
                if v in '-+':
                    sign = 1 if v == '+' else -1
                    continue
                if v == 'x':
                    val += (1 * sign)
                else:
                    val += int(v[:-1]) * sign
            return val
        
        
        def simplify(eq):
            eq = ''.join([v if v not in '+-' else ' ' + v + ' ' for v in eq]).split()
            val, xs = 0, []
            for i in range(len(eq)):
                if eq[i].isnumeric():
                    sign = 1
                    if i:
                        if eq[i-1] == '-':
                            sign = -1
                        xs.pop()
                    val += int(eq[i]) * sign
                else:
                    xs.append(eq[i])
            
            xs = reduce_x(xs)
            return xs, val
            
        
        x_l, v_l = simplify(lhs)
        x_r, v_r = simplify(rhs)
        
        xx = x_l - x_r
        vv = v_r - v_l
        
        if xx == 0 and vv == 0:
            return "Infinite solutions"
        if xx == 0 and vv != 0:
            return "No solution"
        
        if xx < 0:
            xx *= -1
            vv *= -1

        return 'x=' + str(vv//xx) 
