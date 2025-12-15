class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
                
        # return False

        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            hashmap[nums[i]]=i
        
        return False




        




        