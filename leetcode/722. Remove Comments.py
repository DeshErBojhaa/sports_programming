# 722. Remove Comments
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        starind, char_count = -1, 0
        another_contenue = False
        
        for line in source:
            cur_line = ''
            for i in range(len(line)):
                char_count += 1
                if another_contenue:
                    another_contenue = False
                    continue
                if starind > -1:
                    if line[i:i+2] == '*/' and (char_count - 1) - starind > 0:
                        starind = -1
                        another_contenue = True
                        if ans and  ans[-1] and ans[-1][-1] == '∞':
                            cur_line = ans.pop()[:-1] + cur_line
                        elif cur_line and cur_line[-1] == '∞':
                            cur_line = cur_line[:-1]
                    continue
                else:
                    if line[i:i+2] == '/*':
                        starind = char_count
                        if cur_line:
                            cur_line += '∞'
                        continue
                    elif line[i:i+2] == '//':
                        char_count += len(line[i:])
                        break
                cur_line += line[i]

            if cur_line:
                ans.append(cur_line)
        
        return [x for x in ans if x]
