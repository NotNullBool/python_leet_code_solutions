from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i

    raise Exception("There is no two indexes in nums to add to target.")

    # slow
    # for (index, num) in enumerate(nums):
    #     for (inner_index, inner_num) in enumerate(nums):
    #         if index == inner_index:
    #             continue
    #         if num + inner_num == target:
    #             return sorted([index,inner_index])
