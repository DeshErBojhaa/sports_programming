# 721. Accounts Merge
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = defaultdict(list)
        
        # Ω(N)
        for acc in accounts:
            users[acc[0]].append(set(acc[1:]))
        
        def join_rest(cur_set, set_list, seen):
            now_set = set(cur_set)
            for i, v in enumerate(set_list):
                if i in seen or cur_set.isdisjoint(v):
                    continue
                now_set = now_set.union(v)
                seen.add(i)
                rest = join_rest(now_set, set_list, seen)
                now_set = now_set.union(rest)

            return now_set
        
        
        def union(set_list):
            seen = set()
            ans = []
            for i in range(len(set_list)):
                if i in seen:
                    continue
                seen.add(i)
                cur_set = set(set_list[i])
                joined = join_rest(cur_set, set_list, seen)
                cur_set = cur_set.union(joined)
                ans.append(cur_set)
            return ans
        
        ans = []
        for u, emails in users.items():
            merged_emails = union(emails)
            for m_email in merged_emails:
                tmp = [u] + list(sorted(m_email))
                ans.append(tmp)
        
        return ans
