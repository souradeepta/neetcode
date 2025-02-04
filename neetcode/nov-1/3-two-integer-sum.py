class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        T: O(n),
        S: O(n)
        there is a more graceful solution to this without the ladder
        """
        compliment = {}
        for i, n in enumerate(nums):
            compli = target - n
            if n not in compliment:
                compliment[compli] = i
                print(compli, compliment)
            else:
                return [compliment[n], i]


if __name__ == "__main__":
    assert Solution().twoSum([3, 4, 5, 6], 7) == [0, 1]
    assert Solution().twoSum([4, 5, 6], 10) == [0, 2]
