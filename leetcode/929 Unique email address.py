class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            local, domain = e.split('@')
            ff = local.replace('.', '').split('+')[0] + '@'+domain
            # print(ff)
            s.add(ff)
        return len(s)
