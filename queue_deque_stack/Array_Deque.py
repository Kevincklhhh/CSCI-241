from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front_index = 0
    self.__back_index = 0
    self.__size = 0

  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
        return '[ ]'
    to_return = '['
    i = self.__front_index
    while i != self.__back_index:
        to_return += ' ' + str(self.__contents[i]) + ','
        i = (i + 1)%self.__capacity
    to_return += ' ' + str(self.__contents[self.__back_index]) + ' ]'
    return to_return

  def __len__(self):
    return self.__size
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.

  def __grow(self):

    old = self.__contents
    self.__contents = [None] * 2 * self.__capacity
    i = self.__front_index#Use i to walk from front to back of the deque in the old array.
    for j in range(self.__size):
        self.__contents[j] = old[i]
        i = (1 + i) % self.__capacity
    self.__front_index = 0
    self.__back_index = self.__size - 1
    self.__capacity = 2 * self.__capacity

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
        self.__grow()
    self.__front_index = (self.__front_index - 1) % self.__capacity
    self.__contents[self.__front_index] = val
    self.__size += 1



  def pop_front(self):
    if self.__contents[self.__front_index] is not None:
        self.__size -= 1
    if self.__front_index == self.__back_index:#if front and end refers to the same element
        to_return = self.__contents[self.__front_index]
        self.__contents[self.__front_index] = None
        return to_return
    else:
        self.__front_index = (self.__front_index + 1) % self.__capacity
        return self.__contents[(self.__front_index - 1) % self.__capacity]

  def peek_front(self):
    return self.__contents[self.__front_index]

  def push_back(self, val):
    if self.__size == self.__capacity:
        self.__grow()
    self.__back_index = (self.__back_index + 1) % self.__capacity
    self.__contents[self.__back_index] = val
    self.__size += 1



  def pop_back(self):
    if self.__contents[self.__back_index] is not None:
        self.__size -= 1
    if self.__front_index == self.__back_index:#if front and end refers to the same element,the back index does not change after popping
        to_return = self.__contents[self.__back_index]
        self.__contents[self.__back_index] = None
        return to_return
    else:
        self.__back_index = (self.__back_index - 1) % self.__capacity#back_index is decreased by 1, or moved to the end of the array.
        return self.__contents[(self.__back_index + 1) % self.__capacity]

  def peek_back(self):
    return self.__contents[self.__back_index]




# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
