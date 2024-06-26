from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        T: o(nlogn) S: o(n)
        - complexity of most_common(k) is o(nlogk) where
            n number of unique ele in Counter nad k number of ele requested.
        - a.sort() will sort in-place in ascending
        - sorted(a) will not change list
        - reverse=True to get descending
        T: o(nlogk), S: o(n)
        - took 268ms on LC
        """
        count = Counter(nums)
        output = count.most_common(k)
        print(output)
        result = []
        for ele in output:
            print(ele[0])
            result.append(ele[0])
            print(result)
        print(result.sort())
        print(sorted(result))
        return sorted(result)

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        - max heap pop k times which could make it klogn
        - this is bucket sort tho and its O(n)
        - Took 85ms on LCs
        """
        count = {}
        frequency_bucket = [[] for i in range(len(nums)+1)]

        # generate count of items first
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # going through each counted value and add in bucket array
        for n, c in count.items():
            # append the number of elements to the count freq bucket
            frequency_bucket[c].append(n)

        res = []

        # going through all values in desc order essentially 0...n count bucket
        for i in range(len(frequency_bucket) - 1, 0, -1):
            for n in frequency_bucket[i]:
                res.append(n)
                if len(res) == k:
                    print(f"{res=}")
                    return res


if __name__ == "__main__":
    assert Solution().topKFrequent2([1,2,2,3,3,3], 2) == [2,3]
    assert Solution().topKFrequent2([7,7], 1) == [7]