class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # mp = defaultdict(list)
        # res = []

        # for w in strs:
        #     sorted_word = ''.join(sorted(w)) 
        #     if sorted_word in mp:
        #         mp[sorted_word].append(w)
        #     else:
        #         mp[sorted_word] = [w]
        
        # return list(mp.values())

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1
                # [1,0,1,0,0,0.....,1,....,0]

            res[tuple(count)].append(s)
            # gives same exact tuple as other anagrams

        return list(res.values())


        