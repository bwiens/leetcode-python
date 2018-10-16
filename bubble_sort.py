#!/usr/bin/python
#Benjamin Wiens
#Bubble Sort
list = [3, 8, 1, 0, 9, 7, 12, 4]

class Solution():
    def bubblesort(self, list):
        """
        :type list: list
        :rtype: list
        """
        j=1
        swapped = True
        print("unsorted list: ", list)
	#when no swap occured sorting is complete
        while swapped is True:
            swapped = not True
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    #swap
                    list[i], list[i+1] = list[i+1], list[i]
                    print(list)
                    swapped = True
        print(list)
        return list

print(Solution().bubblesort(list))
