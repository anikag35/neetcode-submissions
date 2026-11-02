class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first thoughts: create dict where keys = number, value = count -> sort and return top k keys - O(n log n) time
        # optimization: only possible buckets are 0-n, instead of sorting, collect numbers in buckets

        tracking = {}
        for val in nums:
            if val in tracking:
                tracking[val] += 1
            else:
                tracking[val] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in tracking:
            buckets[tracking[num]].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

