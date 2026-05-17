class Solution:
    OPERATORS = {"+", "-", "*", "/"}

    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in self.OPERATORS:
                    o1 = int(tokens[i - 2])
                    o2 = int(tokens[i - 1])
                    o = tokens[i]
                    r = self.calc(o1, o2, o)
                    tokens = tokens[:i - 2] + [str(r)] + tokens[i+1:]
                    break
         
        return int(tokens[0])

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