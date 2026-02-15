class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output_list = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        seen = {}
        for ind, val in enumerate(nums):
            req = target - val
            if req in seen:
                return [seen[req], ind]
            seen[val] = ind
        



            