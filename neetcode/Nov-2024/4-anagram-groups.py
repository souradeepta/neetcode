from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        generating the key value is the real trick here
        have to use the bitmap to have the ordering of the digits correct.
        T: O(m*n)
        S: O(m), m is number of strings and n is length of the longest string
        """
        result = defaultdict(list)
        for word in strs:
            #     count = Counter(word)
            #     keys = tuple(count.keys())
            #     print(f"{count=} , {keys=}")
            #     if keys not in result.keys():
            #         result[keys].append(word)
            #     else:
            #         result[keys].append(word)
            # print(f"{result=}")
            # return result

            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(word)
        print(result)
        return result.values()


if __name__ == "__main__":
    assert Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["hat"],
        ["act", "cat"],
        ["pots", "stop", "tops"],
    ]
    assert Solution().groupAnagrams(["x"]) == [["x"]]
    assert Solution().groupAnagrams([""]) == [[""]]
