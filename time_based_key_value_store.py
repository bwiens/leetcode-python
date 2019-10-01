# Benjamin Wiens
# Time Based Key Value Store (https://leetcode.com/problems/time-based-key-value-store/)

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = ([(timestamp, value)])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap:
            if len(self.hmap[key]) == 1:
                # check if the timestamp meets the requirements
                if self.hmap[key][0][0] <= timestamp:
                    return self.hmap[key][0][1]
                else:
                    return ''
            else:
                tuples = self.hmap[key]
                # use binary search
                left = 0
                right = len(tuples) -1
                while left <= right:
                    # there's no overflow in python
                    mid = (left + right) // 2
                    if tuples[mid][0] == timestamp:
                        return tuples[mid][1]
                    elif tuples[mid][0] > timestamp:
                        right = mid -1
                    else:
                        left = mid + 1

                if tuples[right][0] <= timestamp:
                    return tuples[right][1]
                return ''
        else:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
