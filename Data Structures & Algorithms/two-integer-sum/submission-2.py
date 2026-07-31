class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [min(i, nums.index(diff)), max(i, nums.index(diff))]
            else:
                hashmap[n] = [i]

