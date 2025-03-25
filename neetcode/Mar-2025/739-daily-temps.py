class Solution:
    """
    - very contrived solution
    - check if top of stack has a lesser value that current temp
        - if yes, then pop the elements in the stack and calculate the diff in positions
        - if no, then just insert it into the stack

    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  # pair [temp, idx]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = idx - stackIdx
            stack.append([temp, idx])

        return result


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
