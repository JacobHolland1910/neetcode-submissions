class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in hashtable:
                hashtable[sorted_str] += [string]
            else:
                hashtable[sorted_str] = [string]
        return list(hashtable.values())