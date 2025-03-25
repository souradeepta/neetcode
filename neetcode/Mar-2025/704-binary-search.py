class Solution:
    """
    - condition has <= and not <
    - famous overflow fix `mid = left + (right- left)//2`
    - remember your recurser should return back the to previous stack
    T: O(logn) S: O(1)
    """

    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def searchR(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        return self.binary_search(left, right, nums, target)

    def binary_search(self, left, right, nums, target):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(mid + 1, right, nums, target)

        return self.binary_search(left, mid - 1, nums, target)


if __name__ == "__main__":
    # assert Solution().searchR([-1,0,3,5,9,12], 9) == 4
    # assert Solution().searchR([-1,0,3,5,9,12], 2) == -1
    assert Solution().searchR([-1, 0, 2, 4, 6, 8], 4) == 3
