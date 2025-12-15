class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}

        # for i in range(len(nums)):
        #     count[nums[i]] = 1 + count.get(nums[i],0)
        # # 1:1, 2:2, 3:3

        # sorted_count = sorted(count.items(),key = lambda x: x[1], reverse = True)
        # # (3,3),(2,2),(1,1)

        # res = []

        # for i in range(0,k):
        #     res.append(sorted_count[i][0])
        
        # return res

### BUCKET SORT ###

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        # {1:1,2:2,3:3}
        
        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                 res.append(n)
                 if len(res) == k: 
                    return res










        