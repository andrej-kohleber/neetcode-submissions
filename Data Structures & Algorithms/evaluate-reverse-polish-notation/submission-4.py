class Solution:
    OPERATORS = {"+", "-", "*", "/"}

    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if self.isOperator(t):
                o2 = int(operands.pop())
                o1 = int(operands.pop())
                r = self.calc(o1, o2, t)
                operands.append(r)
            else:
                operands.append(t)
        return int(operands.pop())


    def isOperator(self, t: str) -> bool:
        return t in self.OPERATORS

    def calc(self, o1: int, o2: int, o: str) -> int:
        if o == "+":
            return o1 + o2
        elif o == "-":
            return o1 - o2
        elif o == "*":
            return o1 * o2
        else:
            return int(o1 / o2)