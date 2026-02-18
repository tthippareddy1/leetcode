class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
            
            
        return list(groups.values())
        






        # sub = set()
        # final = list()
        # for i in range(len(strs)):
        #     m = "".join(sorted(strs[i]))
        #     final.append(m)
            
        # for j in range(len(final)):



        #     for j in range(i+1, len(strs)):
        #         if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
        #             sub.add(strs[i])
        #             sub.add(strs[j])
        #         sub.add(strs[i])
        #         continue             
        #     k = list(sub)
        #     final.append(k)
        #     sub.clear()
        # print(final)


