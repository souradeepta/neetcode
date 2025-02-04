from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        T: o(n), S: o(n)
        """
        compliment = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in compliment:
                result = [compliment[remain], i]
                print(result)
                return result
            else:
                compliment[num] = i
                print(compliment)


if __name__ == "__main__":
    assert Solution().twoSum([3, 4, 5, 6], 7) == [0, 1]
    assert Solution().twoSum([4, 5, 6], 10) == [0, 2]
