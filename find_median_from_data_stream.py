class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        self.list.sort()
        length = len(self.list) 
        if length % 2 == 0:
            return (self.list[len(self.list)//2] + self.list[len(self.list)//2-1]) / 2
        else:
            return self.list[length//2]
                                                     

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
