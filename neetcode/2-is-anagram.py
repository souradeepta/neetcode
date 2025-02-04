class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        T: o(n) S: o(n)
        - sorting would make it nlogn but space is o(1)
        - hack solution: return Counter(s) == Counter(t)
        - slightly better solution would be to create 2 counts and
        just compare them count_a == count_b. last for loop not required.
        """
        if len(s) != len(t):
            return False
        count = {}
        for ele in s:
            if ele not in count:
                count[ele] = 1
            else:
                count[ele] += 1
        print(count)
        for ele in t:
            if ele not in count:
                return False
            else:
                count[ele] -= 1
        print(count)
        total = 0
        for values in count.values():
            total += values
        print(total)
        return total == 0


if __name__ == "__main__":
    assert Solution().isAnagram("racecar", "carrace") is True
    assert Solution().isAnagram("jar", "jam") is False
