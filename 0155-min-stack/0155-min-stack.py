class MinStack:

    def __init__(self):
        self._vals = []
        self._mins = []

    def push(self, val: int) -> None:
        self._vals.append(val)
        if not self._mins or val <= self._mins[-1]: self._mins.append(val)

    def pop(self) -> None:
        if self._mins[-1] == self._vals.pop(): self._mins.pop()

    def top(self) -> int:
        return self._vals[-1]

    def getMin(self) -> int:
        return self._mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()