class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        added, cum_sum = [], 0
        nnn = deque(nums)
        for i in range(nums[-1]+1):
            if not nnn or cum_sum > nums[-1] or cum_sum >= n:
                break
            while nnn and i == nnn[0]:
                cum_sum += nnn.popleft()
            if cum_sum < i:
                added.append(i)
                cum_sum += i

        if cum_sum >= n:
            print(added)
            return len(added)

        arr = sorted(nums + added)
        sm = sum(arr) + 1
        arr.append(sm)

        while arr[-1] < n:
            sm *= 2
            arr.append(sm)

        print(arr)
        return len(arr) - len(nums) - (arr[-1] > n)
