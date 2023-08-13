from typing import List

class Solution:
    def contains_duplicate(self, nums:List[int]) -> bool:
        return (len(nums) != len(set(nums)))

        # too slow for leet code site
    #
        # for index, num in enumerate(nums):
        #     for inner_index, inner_num in enumerate(nums):
        #         if index == inner_index:
        #             continue
        #         if num == inner_num:
        #             return True
        # return False

if __name__ == "__main__":
    solver = Solution()
    print(solver.contains_duplicate([1,2,3]))
    print(solver.contains_duplicate([1,1,2,3]))
