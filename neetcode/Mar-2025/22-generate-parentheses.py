class Solution:
    """
    - intro to backtracking
    T: O(4^n/Root(n))
    S: O(n)
    """
    def generateParenthesis(self, n: int) -> list[str]:
        """
        1. only add open paranthesis if open < n
        2. only add a closing paren if closed < open
        3. valid IF open == closed == n
        """

        stack = []  # global
        result = []

        def backtrack(openN, closedN):
            # 3. condition
            if openN == closedN == n:
                result.append("".join(stack))
                return

            # 1. cond
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # clear the stack because we have completed the tracking
                stack.pop()

            # 2. cond
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    assert Solution().generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
    assert Solution().generateParenthesis(1) == ["()"]