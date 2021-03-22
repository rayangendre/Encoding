
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = [None]
        self.capacity = capacity
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator'''
        if self.is_full():
            return False
        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        temp = self.heap[1]
        self.heap[1], self.heap[self.get_size()] = self.heap[self.get_size()], self.heap[1]
        self.heap.pop()
        self.size -= 1
        self.perc_down(1)
        return temp

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap[1:]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate
        exactly the number of items in alist'''
        self.heap = [0] + alist[:]
        self.size = len(alist)
        if self.capacity < len(alist):
            self.capacity = len(alist)
        i = len(alist) // 2
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.size == 0:
            return True
        return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.capacity == self.size:
            return True
        return False

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i * 2 <= self.size:
            if i * 2 + 1 > self.size or self.heap[i * 2] > self.heap[i * 2 + 1]:
                index = i * 2
            else:
                index = i * 2 + 1

            if self.heap[i] < self.heap[index]:
                self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            i = index

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        while len(alist) != 0:
            alist.pop()
        while not self.is_empty():
            alist.insert(0, self.dequeue())
        self.build_heap(alist)





