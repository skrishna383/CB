class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
                    
                    
                    
#M2 heaps
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = {}
        min_heap = []

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for num, freq in frequency_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq,num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, num))
        top_k_frequent = [num for freq, num in min_heap]
        return top_k_frequent