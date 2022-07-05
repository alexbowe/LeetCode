class MinStack:

    def __init__(self):
        self._min_stack = []
        self._stack = []
        

    def push(self, val: int) -> None:
        if not self._min_stack or val <= self._min_stack[-1]: self._min_stack.append(val)
        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_stack[-1]: self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()