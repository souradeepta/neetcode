from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        T: O(n+m)
        S: 0(1) constant space n+m
        optimal using bit set for 26
        """
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t


if __name__ == "__main__":
    assert Solution().isAnagram("racecar", "carrace") is True
    assert Solution().isAnagram("jar", "jam") is False
