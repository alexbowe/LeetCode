class MyQueue:

    def __init__(self):
        self._inbox = []
        self._outbox = []

    def push(self, x: int) -> None:
        self._inbox.append(x)

    def pop(self) -> int:
        self.peek()
        return self._outbox.pop()

    def peek(self) -> int:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
        return self._outbox[-1]

    def empty(self) -> bool:
        return not self._inbox and not self._outbox


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()