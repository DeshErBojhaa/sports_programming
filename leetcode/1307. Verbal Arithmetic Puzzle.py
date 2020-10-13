# 1307. Verbal Arithmetic Puzzle
class Solution:
    def isSolvable(self, words, result):
        words.append(result)
        R, C = len(words), max(map(len, words))

        to_int = {}
        to_chr = [None] * 10

        def search(r, c, bal):
            if c == C:
                return bal == 0
            if r == R:
                res, rem = divmod(bal, 10)
                return rem == 0 and search(0, c+1, res)

            if c >= len(words[r]):
                return search(r+1, c, bal)

            letter = words[r][~c]
            sign = -1 if r == R-1 else 1
            
            if letter in to_int:
                if to_int[letter] or len(words[r]) == 1 or c != len(words[r]) - 1:
                    return search(r+1, c, bal + (sign * to_int[letter]))
                return False
            else:
                for num, ch in enumerate(to_chr):
                    if ch is not None or (num == 0 and c == len(words[r]) - 1):
                        continue
                    to_chr[num] = letter
                    to_int[letter] = num

                    if search(r+1, c, bal + (sign * num)):
                        return True

                    to_chr[num] = None
                    del to_int[letter]

            return False

        return search(0, 0, 0)
        
