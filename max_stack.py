# Benjamin Wiens
# Max Stack (https://leetcode.com/problems/max-stack/)

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        if self.stack:
            maximum = self.stack[0]
            to_remove = None
            for index, s in enumerate(self.stack):
                if maximum <= s:
                    maximum = s
                    to_remove = index
            del self.stack[to_remove]
            return maximum
            


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
