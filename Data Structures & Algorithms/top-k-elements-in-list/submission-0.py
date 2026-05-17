class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        sorted_keys = sorted(count, reverse=True, key=lambda x:count[x])
        
        return sorted_keys[:k]
        
        