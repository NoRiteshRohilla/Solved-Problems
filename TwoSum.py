
#leetcode solution: -> 1

def solve(n, nums, target):
    m = {}
    for i, el in enumerate(nums):
        if target - el in m:
            return [m[target-el], i]
        m[el] = i
        
