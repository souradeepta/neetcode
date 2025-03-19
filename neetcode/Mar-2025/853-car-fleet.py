class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pass


if __name__ == "__main__":
    assert Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) ==3
    assert Solution().carFleet(10, [3], [2,4,1,1,3]) == 1
    assert Solution().carFleet(100, [0, 2, 4], [4,2,1]) == 1
