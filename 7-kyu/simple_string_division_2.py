def solve(s,k):
    nums = s.split()
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                concated = nums[i] + nums[j]
                if int(concated) % k == 0:
                    count += 1
                    
    return count
