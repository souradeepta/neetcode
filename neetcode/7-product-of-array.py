from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    assert Solution().productExceptSelf([1,2,4,6]) == [48,24,12,8]
    assert Solution().productExceptSelf([-1,0,1,2,3]) == [0,-6,0,0,0]