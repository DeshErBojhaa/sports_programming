def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people = sorted(people)
        ans = [(-1,-1) for _ in range(len(people))]
        
        # print(people)
        for h, pos in people:
            e_or_ge = 0
            for i in range(len(ans)):
                if ans[i][0] == -1 or ans[i][0] >= h:
                    e_or_ge += 1
                if e_or_ge == pos+1:
                    ans[i] = (h, pos)
                    break
        return ans
