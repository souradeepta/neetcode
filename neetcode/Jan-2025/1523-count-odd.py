class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # find odds, remember high inclusive
        # this solution goes TLE
        # count = 0
        # for i in range(low, high+1):
        #     if i % 2 != 0:
        #         count += 1
        # print(f"{count=}")
        # return count
        return (high - low + 1) // 2 if low % 2 == 0 else (high - low) // 2 + 1


if __name__ == "__main__":
    assert Solution().countOdds(3, 7) == 3
    assert Solution().countOdds(8, 10) == 1
