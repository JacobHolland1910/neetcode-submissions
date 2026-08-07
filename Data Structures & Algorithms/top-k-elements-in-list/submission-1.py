class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        final_list = []
        for k in range(k):
            final_list.append(list(sorted_hashmap)[k])
        return final_list

            
        