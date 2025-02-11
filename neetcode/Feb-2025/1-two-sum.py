class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        - remember what to save in the compliment
        - check if numbers to be returned or indices
        - dont need a branch commented.
        T: O(n) n = traverse each elements only once if required.
        S: O(n) n = number of items stored in hash map
        """
        compliment = {}
        for i, num in enumerate(nums):
            if target - num in compliment:
                return [compliment[target - num], i]
            # else:
            #     compliment[num] = i
            compliment[num] = i

        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
