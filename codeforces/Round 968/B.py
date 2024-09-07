if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        nums = sorted(map(int, input().split()))
        if len(nums) < 3:
            print(nums[-1])
            continue
        print(nums[len(nums)//2])
