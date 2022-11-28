class MyQueue:

    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self.peek()
        return self._out.pop()

    def peek(self) -> int:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out[-1]

    def empty(self) -> bool:
        return not (self._in or self._out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()