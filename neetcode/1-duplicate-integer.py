class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        T: o(n), S: o(n)
        - sorting would make it nlogn but constant space
        """
        count = set()
        for num in nums:
            if num not in count:
                count.add(num)
            else:
                return True
        return False


if __name__ == '__main__':
    assert Solution().hasDuplicate([1, 2, 3, 1]) is True
    assert Solution().hasDuplicate([1, 2, 3, 4]) is False