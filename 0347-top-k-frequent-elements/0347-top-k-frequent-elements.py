class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            group[num] = group.get(num,0)+1
        
        sorted_dic = dict(sorted(group.items(), key = lambda item: item[1], reverse = True))
        sorted_keys = list(sorted_dic.keys())
        return sorted_keys[:k]
        # final = []
        # for i in range(k):
        #     final.append(sorted_keys[i])
        # return final
            


        
        

        # values = list(group.values())
        # values.sort(reverse = True)
        # final = []
        # for val in values[:k]:
        #     final.append(group[val])



        # keys = list(group.keys())
        # final = []
        
        # for val in range(k):
        #     final.append(keys[val])
        # return final
            
           