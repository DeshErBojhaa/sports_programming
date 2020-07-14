# 68. Text Justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, cur = [], ''
        
        for w in words:
            if not cur:
                cur = w
                continue
            if len(cur) + len(w) + 1 <= maxWidth:
                cur += ' ' + w
            else:
                ans.append(cur.lstrip())
                cur = w
        
        if cur:
            ans.append(cur.lstrip())
        
        for i in range(len(ans)-1):
            word_this_line = ans[i].split()
            used_len = sum(map(len, word_this_line))
            spaces = maxWidth - used_len
            per_word = spaces // max(1, len(word_this_line) - 1)
            extra = spaces - (per_word * max(1, len(word_this_line)-1))
            
            line = ''
            for w in word_this_line[:-1]:
                line += w + ' ' * per_word
                if extra > 0:
                    extra -= 1
                    line += ' '
            line += word_this_line[-1]
            
            line += ' ' * (maxWidth - len(line)) # For lines consists of only one word
            ans[i] = line
        
        last_line = ans[-1]
        last_line += ' ' * (maxWidth - len(last_line))
        ans[-1] = last_line
        
        return ans
        
        
