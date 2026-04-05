"""Maximum Frequency Stack"""

class Node:
    """
    Represents a single node in a linked list.
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    """
    A LIFO stack implementation using a linked list.
    """
    def __init__(self):
        self.stack = None
        self.size = 0

    def is_empty(self):
        """
        Returns True if the stack is empty.
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
        Removes and returns the top element.
        """
        val = None
        if self.stack:
            val = self.stack.val
            self.stack = self.stack.next
            self.size -= 1
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
        return self.size

    def __str__(self):
        if not self.stack:
            return 'There is no information'
        res = 'Information: '
        prob = self.stack
        while prob:
            res += str(prob.val)
            prob = prob.next
        return res

class FreqStack(object):
    """
    Stack that pops the most frequent element.
    """

    def __init__(self):
        """
        Initializes frequency dictionary and stacks.
        """
        self.freq_dic = {}
        self.biggest_freq = None
        self.freq_stack_dic = {}

    def push(self, val):
        """
        Pushes a value and updates its frequency.
        :type val: int
        :rtype: None
        """
        if not self.freq_stack_dic:
            self.freq_stack_dic[1] = Stack()
            self.freq_stack_dic[1].push(val)
            self.freq_dic[val] = 1
            self.biggest_freq = 1
        else:
            if not val in self.freq_dic:
                self.freq_dic[val] = 1
                self.freq_stack_dic[1].push(val)
            else:
                self.freq_dic[val] += 1
            if not self.freq_dic[val] in self.freq_stack_dic:
                self.freq_stack_dic[self.freq_dic[val]] = Stack()
                self.freq_stack_dic[self.freq_dic[val]].push(val)
            else:
                self.freq_stack_dic[self.freq_dic[val]].push(val)
            if self.freq_dic[val] > self.biggest_freq:
                    self.biggest_freq = self.freq_dic[val]

    def pop(self):
        """
        Pops the most frequent element.
        :rtype: int
        """
        val = self.freq_stack_dic[self.biggest_freq].pop()
        self.freq_dic[val] -= 1
        if self.freq_stack_dic[self.biggest_freq].is_empty():
            if self.biggest_freq - 1 in self.freq_stack_dic:
                self.biggest_freq -= 1
            else:
                while not self.biggest_freq - 1 in self.freq_stack_dic:
                    self.biggest_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
