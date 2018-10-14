#!/usr/bin/python
#Benjamin Wiens
#Linked List
#Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#If there are two middle nodes, return the second middle node.

import math

#each node needs the data field and the next field
class Node:
    def __init__(self, data):
        self.data = data
        #initially next points to None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def insert (self, newNode):
        #if the head is empty make the new node a head node
        if self.head is None:
            self.head = newNode
        else:
            #go through nodes until next is none
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        #start from the head node until we reach the middle
        currentNode = self.head
        c = 0.0
        while True:
            # break if last node
            if currentNode is None:
                middle = (math.floor(c/2))
                #print(middle)
                break
            c += 1
            #print(currentNode.data)
            currentNode = currentNode.next
        #go through list again and print only the middle
        currentNode = self.head
        for i in range(middle):
            currentNode = currentNode.next
        print(currentNode.data)

linkedList = LinkedList()
firstNode = Node(1)
linkedList.insert(firstNode)
secondNode = Node(2)
linkedList.insert(secondNode)
thirdNode = Node(3)
linkedList.insert(thirdNode)
fourthNode = Node(4)
linkedList.insert(fourthNode)
fifthNode = Node(5)
linkedList.insert(fifthNode)
sixthNode = Node(6)
linkedList.insert(sixthNode)
linkedList.printList()
