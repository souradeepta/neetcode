class Solution:
    """
    Mistakes:
    - forgot base case of match
    - forgot to cast the strs to ints
    """
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = ('+', '-', '*', '/')

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                second = stack.pop() if stack else 0
                first = stack.pop() if stack else 0
                output = self.calculate(first, second, token)
                stack.append(output)

        return stack[0] if stack else None

    def calculate(self, first, second, operand):
        match operand:
            case '+':
                result = first + second
            case '-':
                result = first - second
            case '/':
                # result = first // second
                result = int(float(first / second))
            case '*':
                result = first * second
            case _:
                raise ValueError('Invalid Operator')

        return result


if __name__ == "__main__":
    assert Solution().evalRPN(["2","1","+","3","*"]) == 9
    assert Solution().evalRPN(["4","13","5","/","+"]) == 6