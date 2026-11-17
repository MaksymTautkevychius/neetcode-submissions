class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        returned = []
        for i in nums:
            values[i] = values.get(i, 0) + 1
        
        sorted_items = sorted(values.items(), key=lambda x: x[1], reverse=True)

            
        for i in range(k):
            returned.append(sorted_items[i][0])
        return returned

