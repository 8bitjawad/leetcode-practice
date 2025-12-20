class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = r = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            window_length = r-l+1
            max_freq = max(count.values())

            temp = window_length - max_freq
            if temp <= k:
                res = max(res, window_length)
            else:
                while (r-l+1) - max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1

        return res
            

        