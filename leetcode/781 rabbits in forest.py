def numRabbits(self, answers: List[int]) -> int:
        a = 0
        c = Counter(answers)
        
        for ans, num in c.items():
            n = num // (ans+1)
            n += int(num%(ans+1) != 0)
            a += n * (ans+1)
        return a
