# 273. Integer to English Words
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        d = {
            1000000000 : 'Billion',
            1000000: 'Million',
            1000: 'Thousand',
            100: 'Hundred',
            90 : 'Ninety',
            80 : 'Eighty',
            70 : 'Seventy',
            60 : 'Sixty',
            50 : 'Fifty',
            40 : 'Forty',
            30 : 'Thirty',
            20 : 'Twenty',
            19 : 'Nineteen',
            18 : 'Eighteen',
            17 : 'Seventeen',
            16 : 'Sixteen',
            15 : 'Fifteen',
            14 : 'Fourteen',
            13 : 'Thirteen',
            12 : 'Twelve',
            11 : 'Eleven',
            10 : 'Ten',
            9 : 'Nine',
            8 : 'Eight',
            7 : 'Seven',
            6 : 'Six',
            5 : 'Five',
            4 : 'Four',
            3 : 'Three',
            2 : 'Two',
            1 : 'One'
        }
        
        ans = []
        def to_english(n):
            nonlocal ans
            if n < 1:
                return []
            if n in d and n < 100:
                return [d[n]]
            
            tmp = []
            for k, v in d.items():
                full, rem = divmod(n, k)
                if full > 0 and rem > 0:
                    if n > 99:
                        tmp.extend(to_english(full))
                        tmp.append(v)
                        tmp.extend(to_english(rem))
                    else:
                        tmp.append(v)
                        tmp.extend(to_english(rem))
                    return tmp
                elif full > 0 and rem == 0:
                    if k == 1000000000 or k == 1000000 or k == 1000 or k == 100:
                        tmp.extend(to_english(full))
                        tmp.append(v)
                        return tmp
                    return [v]
            
            return []
        
        return ' '.join(to_english(num))
