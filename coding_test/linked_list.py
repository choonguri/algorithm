# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def ReversePrint(head):  # function name should be lowercase!
    if head is None:
        return

    ReversePrint(head.next)
    print(head.data)