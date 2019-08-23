# Benjamin Wiens
# Logger Rate Limiter (https://leetcode.com/problems/logger-rate-limiter/)

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp or timestamp == 0:
            if message in self.hmap:
                passed = self.hmap.get(message)
                if abs(timestamp - passed) > 9:
                    self.hmap[message] = timestamp
                    return True
                else:
                    return False
            else:
                self.hmap[message] = timestamp
                return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
