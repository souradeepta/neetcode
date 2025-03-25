class Solution:
    def isValid(self, s: str) -> bool:
        """
        Mistakes:
        - in remember mapping is closed bracs to open
        - in not checking if stack is empty
        - not returning False to quit immediately if mapping does not match.
        T: o(n), S: o(n)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack and mapping.get(char) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([])") is True
