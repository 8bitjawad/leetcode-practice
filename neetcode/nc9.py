class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        myset = set(nums)

        def backtrack(num):
            i = 0
            while num in myset:
                num += 1
                i += 1
            return i

        length = 0
        for num in myset:
            if (num-1) not in myset:
                curr_val = num
                curr_length = backtrack(curr_val)
                length = max(length, curr_length)

        return length

        