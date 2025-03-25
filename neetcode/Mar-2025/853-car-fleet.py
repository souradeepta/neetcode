class Solution:
    """
    - didnt approach that sorting by distance would fix the poping of stack problem.

    T: O(N), S: O(N)
    """

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # stack = []  # [pos, speed]
        # for i in range(len(position)):
        #     currP = position[i] + speed[i]
        #     stack.append([currP, speed[i]])

        # stack = sorted(stack)
        # left, right = 0, len(stack)
        # while left < right-1:
        #     if stack[left][0] == stack[left+1][0]:
        #         if stack[left][0] < target:
        #             stack.pop()

        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:  # reverse from highest position
            stack.append((target - p) / s)  # distance / speeed
            if (
                len(stack) >= 2 and stack[-1] <= stack[-2]
            ):  # head of stack forms a fleet
                stack.pop()

        return len(stack)


if __name__ == "__main__":
    assert Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert Solution().carFleet(10, [3], [2, 4, 1, 1, 3]) == 1
    assert Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
