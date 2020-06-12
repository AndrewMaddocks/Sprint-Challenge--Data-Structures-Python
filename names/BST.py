

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        if value == self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left is None:
                return False
            else:
                if self.left.contains(target):
                    return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                if self.right.contains(target):
                    return True
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            max_value = self.value
            return max_value
        elif self.value < self.right.value:
            max_value = self.right.get_max()
            return(max_value)

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

        # build up your call stack to see what happens

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # dont use recusion use a queue with a while loop

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # use a queue

    # start queue with root node
    # while loop that checks
    # size of queue
        # pointer variable
        # that updates at the
        # begging of each loop

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        current = node
        stack = Stack()
        stack.push(current)
        while stack.__len__() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.right:
                stack.push(popped.right)
            if popped.left:
                stack.push(popped.left)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
