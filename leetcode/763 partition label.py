def partitionLabels(self, S: str) -> List[int]:
        last_ind = {}
        for i, c in enumerate(S):
            last_ind[c] = i
        
        ans = []
        last_str_end = -1
        cur_str_end = 0
        for i, c in enumerate(S):
            cur_str_end = max(cur_str_end, last_ind[c])
            if i == cur_str_end:
                ans.append(cur_str_end - last_str_end)
                last_str_end = i
        
        
        return ans
