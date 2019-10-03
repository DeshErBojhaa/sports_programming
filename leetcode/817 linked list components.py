def numComponents(self, head: ListNode, G: List[int]) -> int:
        par = [i for i in range(10001)]
        def find_par(x):
            while par[x] != x:
                x = find_par(par[x])
            return x
        
        s = set(G)
        ans = 0
        if not head: return 0
        if not head.next: return int(head.val in G)
        
        runner = head.next
        
        while runner:
            # print(head.val, runner.val)
            if head.val in s and runner.val in s:
                par[find_par(head.val)] = find_par(runner.val)
            head = runner
            runner = runner.next
        heads = set()
        for x in G:
            heads.add(find_par(x))
        return len(heads)
