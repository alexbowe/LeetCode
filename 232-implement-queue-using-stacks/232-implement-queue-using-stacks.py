class MyQueue:
    def __init__(self):
        self._input = []
        self._output = []

    def push(self, x: int) -> None:
        self._input.append(x)

    def pop(self) -> int:
        self.peek()
        return self._output.pop()

    def peek(self) -> int:
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())
        return self._output[-1]

    def empty(self) -> bool:
        return len(self._input) == 0 and len(self._output) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()