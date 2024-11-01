from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        T: o(n^2), S: o(n)
        - sets are not guarantteed to bew sorted and unhashable
        - complexity of converting a list to a set is o(n)
        - sort based on lexo and on length to match assert
        """
        group = defaultdict(list)
        for s in strs:
            group[(frozenset(s))].append(s)
        print(group)

        result = []
        for key, value in group.items():
            result.append(value)
        for ele in result:
            ele.sort()
        print(result)
        result.sort(key=lambda x: len(x))
        print(result)
        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        T: o(m*n) where m = number of strings and n = average length of each str
        - complexity of converting a list to tuple is n
        """
        result = defaultdict(list)
        for s in strs:
            # since only small chars
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(s)
        print(result.values())
        return result.values()


if __name__ == "__main__":
    assert Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]) == \
        [["hat"],["act", "cat"],["pots","stop", "tops"]]
    assert Solution().groupAnagrams(["x"]) == [["x"]]
    assert Solution().groupAnagrams([""]) == [[""]]