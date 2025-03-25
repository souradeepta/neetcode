class Solution:
    """
    - very convoluted question.
    - must know logic to solve
    """

    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair (idx, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index  # extending backwards since we found a new height
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == "__main__":
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea([2, 4]) == 4
