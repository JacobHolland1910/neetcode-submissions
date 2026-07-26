class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number not in hashset:
                hashset.add(number)
            elif number in hashset:
                return True
        return False