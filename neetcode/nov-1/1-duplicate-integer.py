class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """1-duplicate-integer.py
        T: O(n)
        S: O(n)
        """
        length = len(nums)
        non_dup_len = len(set(nums))
        return True if length > non_dup_len else False


if __name__ == "__main__":
    assert Solution().hasDuplicate([1, 2, 3, 1]) is True
    assert Solution().hasDuplicate([1, 2, 3, 4]) is False
