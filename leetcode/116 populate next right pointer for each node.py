def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()    
        root.next = None
        q.append(root)

        while q:
            v = [i.val for i in q]
            # print(v)
            nx = []
            for x in range(len(q)):
                if x+1 < len(q):
                    q[x].next = q[x+1]
                else:
                    q[x].next = None
                    
                if q[x].left:
                    nx.append(q[x].left)
                    nx.append(q[x].right)

            if nx:
                q = deque(nx)
            else:
                break
        
        return root
