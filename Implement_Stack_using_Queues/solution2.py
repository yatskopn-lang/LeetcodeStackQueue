"""Implement Stack using Queues"""

class Node:
    """
    Represents a single node in a linked list.
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    """
    A FIFO (First-In-First-Out)
    queue implementation using a linked list.
    """
    def __init__(self):
        self.queue = None
        self.size = 0
    def is_empty(self):
        """
        Returns True if the queue
        contains no elements.
        """
        return self.queue is None
    def add(self, item):
        """
        Adds an element to the back of the queue.
        """
        if not self.queue:
            self.queue = Node(item)
        else:
            prob = self.queue
            while prob and prob.next:
                prob = prob.next
            prob.next = Node(item)
        self.size += 1
    def pop(self):
        """
        Removes and returns the
        front element of the queue.
        """
        val = None
        if self.queue:
            val = self.queue.val
            self.queue = self.queue.next
            self.size -= 1
        return val
    def peek(self):
        """
        Returns the front element of
        the queue without removing it.
        """
        val = None
        if self.queue:
            val = self.queue.val
        return val
    def __len__(self):
        """
        Returns the number of elements in the queue.
        """
        return self.size
    def __str__(self):
        """
        Returns a string representation
        of all elements in the queue.
        """
        if not self.queue:
            return 'There is no information.'
        res = 'Information: '
        prob = self.queue
        while prob:
            res += str(prob.val)
            prob = prob.next
        return res

class MyStack(object):
    """
    A LIFO (Last-In-First-Out) stack
    implementation using two queues.
    """
    def __init__(self):
        """
        Initializes two internal queues
        to manage stack operations.
        """
        self.stack1 = Queue()
        self.stack2 = Queue()
    def push(self, x):
        """
        Pushes element x onto the top of the stack.
        Logic: Adds new element to stack2, then
        moves all elements from stack1
        to stack2 to maintain LIFO order, and swaps the queues.
        :type x: int
        :rtype: None
        """
        self.stack2.add(x)
        while self.stack1.queue:
            val = self.stack1.pop()
            self.stack2.add(val)
        stack1 = self.stack1
        stack2 = self.stack2
        self.stack1 = stack2
        self.stack2 = stack1
    def pop(self):
        """
        Removes the element on the top of the
        stack and returns it.
        :rtype: int
        """
        return self.stack1.pop()
    def top(self):
        """
        Returns the element on the top
        of the stack without removing it.
        :rtype: int
        """
        return self.stack1.peek()
    def empty(self):
        """
        Returns True if the stack is
        empty, False otherwise.
        :rtype: bool
        """
        return self.stack1.is_empty() and self.stack2.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
