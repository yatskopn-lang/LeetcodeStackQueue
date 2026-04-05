"""Implement Queue using Stacks"""

class Node:
    """Represents a single node in a linked list."""
    def __init__(self, val, next_el=None):
        self.val = val
        self.next = next_el

class Stack:
    """
    A LIFO (Last-In-First-Out) stack
    implementation using a linked list.
    """
    def __init__(self):
        self.stack = None
        self.size = 0

    def is_empty(self):
        """
        Returns True if the stack has no elements.
        """
        return self.stack is None

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.stack = Node(item, self.stack)
        self.size += 1

    def pop(self):
        """
        Removes and returns the top element of the stack.
        """
        val = None
        if self.stack:
            val = self.stack.val
            self.stack = self.stack.next
        return val

    def peek(self):
        """
        Returns the top element without removing it.
        """
        val = None
        if self.stack:
            val = self.stack.val
        return val

    def __len__(self):
        """
        Returns the current number
        of elements in the stack.
        """
        return self.size

    def __str__(self):
        """
        Returns a string representation
        of the stack elements.
        """
        res = ''
        if self.stack:
            prob = self.stack
            while prob:
                res += str(prob.val)
                prob = prob.next
        if not res:
            return "There is no elements."
        return 'Elements:' + res

class MyQueue(object):
    """
    A FIFO (First-In-First-Out)
    queue implementation using two stacks.
    """

    def __init__(self):
        """
        Initializes two internal stacks:
        one for push and one for pop operations.
        """
        self.queue_push = Stack()
        self.queue_pop = Stack()

    def push(self, x):
        """
        Pushes element x to the back of the queue.
        :type x: int
        :rtype: None
        """
        self.queue_push.push(x)

    def pop(self):
        """
        Removes the element from
        the front of the queue and returns it.
        :rtype: int
        """
        if self.queue_pop.is_empty():
            while not self.queue_push.is_empty():
                val = self.queue_push.pop()
                self.queue_pop.push(val)
        return self.queue_pop.pop()
    def peek(self):
        """
        Returns the element at the front
        of the queue without removing it.
        :rtype: int
        """
        if self.queue_pop.is_empty():
            while not self.queue_push.is_empty():
                val = self.queue_push.pop()
                self.queue_pop.push(val)
        return self.queue_pop.peek()

    def empty(self):
        """
        Returns True if the queue
        is empty, False otherwise.
        :rtype: bool
        """
        return self.queue_pop.is_empty() and self.queue_push.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
