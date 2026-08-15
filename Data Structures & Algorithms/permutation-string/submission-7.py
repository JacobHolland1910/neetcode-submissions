class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sets1 = set()
        lists1 = list(s1)
        for l in lists1:
            if l not in sets1:
                sets1.add(l)
        
        l, r = 0, 0
        while r < len(s2) and l <= len(s2)-len(s1):
            if s2[l] in sets1:
                listsub = []
                for _ in range(len(s1)):
                    listsub.append(s2[r])
                    r += 1
                if sorted(listsub) == sorted(lists1):
                    return True
                else:
                    l += 1
                    r = l
            else:
                l += 1
                r += 1
        return False

