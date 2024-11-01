from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # left, seq, right = 0, 0, len(nums)-1
        # while left < right:
        #     print(f"{left=}, {right=}, {seq}")
        #     if nums[left] + 1 == nums[left+1]:
        #         seq += 1
        #     left += 1

        # return seq
        unique = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in unique:
                length = 1
                while (num+length) in nums:
                    length += 1
                longest = max(length, longest)
        print(longest)
        return longest



if __name__ == "__main__":
    assert Solution().longestConsecutive([2,20,4,10,3,4,5]) == 4
    assert Solution().longestConsecutive([0,3,2,5,4,6,1,1]) == 7