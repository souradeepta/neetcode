from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        count = Counter(nums)
        freq = count.most_common(k)
        for elem in freq:
            result.append(elem[0])

        print(f"{freq=}, {result=}")
        return result


if __name__ == "__main__":
    assert Solution().topKFrequent([1,2,2,3,3,3], 2) == [2,3]
    assert Solution().topKFrequent([7,7], 1) == [7]