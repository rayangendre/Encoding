class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.list = Node(None)
        self.list.next = self.list
        self.list.prev = self.list


    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.list.next == self.list and self.list.prev == self.list:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        new_item = Node(item)
        if self.is_empty():
            new_item.next = self.list
            new_item.prev = self.list
            self.list.next = new_item
            self.list.prev = new_item
            return True

        iterator = self.list.next
        while item != iterator.item:
            if iterator.item is None or item < iterator.item:
                new_item.next = iterator
                new_item.prev = iterator.prev
                iterator.prev.next = new_item
                iterator.prev = new_item
                return True
            elif item > iterator.item:
                iterator = iterator.next
        return False

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        iterator = self.list.next
        while iterator is not self.list:
            if iterator.item == item:
                iterator.prev.next = iterator.next
                iterator.next.prev = iterator.prev
                return True
            iterator = iterator.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        current_node = self.list.next
        while current_node is not self.list:
            if current_node.item == item:
                return index
            index += 1
            current_node = current_node.next
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")
        iterator = self.list.next
        current_index = 0
        while iterator is not self.list:
            if current_index == index:
                iterator.prev.next = iterator.next
                iterator.next.prev = iterator.prev
                return iterator.item
            current_index += 1
            iterator = iterator.next

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.list.next, item)

    def search_helper(self, node, item):
        if node is self.list:
            return False
        elif node.item == item:
            return True
        return self.search_helper(node.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        current_val = self.list.next
        rep_list = []
        while current_val is not self.list:
            rep_list.append(current_val.item)
            current_val = current_val.next
        return rep_list

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.list.prev, [])

    def python_list_reversed_helper(self, current_list, rev_list):
        if current_list is self.list:
            return rev_list
        rev_list.append(current_list.item)
        return self.python_list_reversed_helper(current_list.prev, rev_list)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.list.next)

    def size_helper(self, node):
        if node is None or node is self.list:
            return 0
        return self.size_helper(node.next) + 1