# 833. Find And Replace in String
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans, instructions = [], {}
        
        for i, s, r in zip(indexes, sources, targets):
            instructions[i] = (s, r, len(s))
        
        i = 0
        while i < len(S):
            if i not in instructions:
                ans.append(S[i])
            elif instructions[i][0] == S[i:i+instructions[i][2]]:
                ans.append(instructions[i][1])
                i = i + instructions[i][2] - 1
            else:
                ans.append(S[i])
            i += 1
        return ''.join(ans)
