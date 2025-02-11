from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - can divide by zero
        """
        product = 1
        for num in nums:
            product *= num
        print(f"{product=}")
        for idx, num in enumerate(nums):
            if num != 0:
                nums[idx] = product // num
                print(f"{nums=}")
        return nums

        # nums2 = copy.deepcopy(nums)
        # for idx, num in enumerate(nums):
        #     for i in range(len(nums)):
        #         nums[idx] = 1
        #         if i != idx:
        #             nums[idx] *= nums2[i]
        #             print(f"{nums}")

        # return nums

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        """
        T :o(n), S: o(1)
        """
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == "__main__":
    assert Solution().productExceptSelf2([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert Solution().productExceptSelf2([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]
