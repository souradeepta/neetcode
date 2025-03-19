class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for num in nums:
            
        return result


if __name__ == "__main__":
    assert Solution().productExceptSelf2([1,2,4,6]) == [48,24,12,8]
    assert Solution().productExceptSelf2([-1,0,1,2,3]) == [0,-6,0,0,0]