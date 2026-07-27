class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joinedlist = int("".join(map(str, digits)))
        joinedlist += 1
        return list(map(int, str(joinedlist)))
        