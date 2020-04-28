class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        ans = []
        
        def trav(cur, tmp_ans):
            # print(cur, tmp_ans)
            if cur > len(s):
                return
            if cur == len(s):
                if len(tmp_ans.split('.')) == 4:
                    ans.append(tmp_ans)
                return
            
            if len(tmp_ans.split('.')) == 4:
                return
            
            this_slot = ''
            if tmp_ans:
                tmp_ans += '.'
            for c in s[cur:]:
                this_slot += c
                if int(this_slot) > 255:
                    break
                if int(this_slot) == 0:
                    return trav(cur+len(this_slot), tmp_ans + this_slot)    
                trav(cur+len(this_slot), tmp_ans + this_slot)
        
        trav(0, '')
        return ans
