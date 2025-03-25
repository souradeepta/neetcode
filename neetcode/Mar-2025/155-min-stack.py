class MinStack:
    """
    Mistakes:
    - kept forgetting to write self.
    - fogot to check if stack valid in getMin method
    - wrong output on [0,1,0]; on pop() getMin having only 0 now has None
    But should return 0
    - pop does not return anything
    T: O(1), S: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # when pushing find the min
        self.stack.append(val)

        # if not self.min_stack:
        #     self.min_stack.append(val)

        # if self.min_stack and self.min_stack[-1] > val:
        #     self.min_stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        # when poping find the new min
        # last = self.stack.pop()
        # if self.min_stack and self.min_stack[-1] == last:
        #     self.min_stack.pop()
        # return last
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


def main():
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(4)
    # print(obj.getMin())
    # obj.push(3)
    # print(obj.getMin())
    # obj.push(2)
    # print(obj.getMin())
    # print(obj.top())
    # obj.pop()
    # print(obj.getMin())
    # obj.push(1)
    # print(obj.top())
    # print(obj.getMin())

    obj = MinStack()
    obj.push(0)
    print(obj.getMin())
    obj.push(1)
    print(obj.getMin())
    obj.push(0)
    print(obj.getMin())
    print(obj.top())
    obj.pop()
    print(obj.getMin())
    print(obj.top())
    print(obj.getMin())


if __name__ == "__main__":
    main()
