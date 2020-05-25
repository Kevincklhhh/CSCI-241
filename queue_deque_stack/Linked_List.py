class Linked_List:

  class __Node:

    def __init__(self, val):#initiate node object
      self.value = val
      self.prev = None
      self.next = None


  def __init__(self):#Define attributes of linked list instance.
    self.__size = 0
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header

  def __len__(self):
    return self.__size

  def append_element(self, val):
      element = self.__Node(val)
      element.prev = self.__trailer.prev
      element.next = self.__trailer
      self.__trailer.prev.next = element
      self.__trailer.prev = element
      self.__size = self.__size + 1


  def insert_element_at(self, val, index):
    if index >= self.__size or index < 0:##raise exception for out-of-bound input.
        raise IndexError
    element = self.__Node(val)
    if index < self.__size/2:
        cur = self.__header.next
        for i in range(index):#go to the current element with given index
            cur = cur.next
    else:#if the given index is in the second half, start from trailer.
        cur = self.__trailer.prev
        for i in range(self.__size-1-index):#go to the current element with given index.
            cur = cur.prev
    cur.prev.next = element
    element.next = cur
    element.prev = cur.prev
    cur.prev = element
    self.__size = self.__size + 1


  def remove_element_at(self, index):
    if index >= self.__size or index < 0:#raise exception for out-of-bound input.
        raise IndexError
    if index < self.__size/2:
        to_remove = self.__header.next
        for i in range(index):#go to the current element with given index.
            to_remove = to_remove.next
    else:#if the given index is in the second half, start from trailer.
        to_remove = self.__trailer.prev
        for i in range(self.__size-1-index):#go to the current element with given index
            to_remove = to_remove.prev
    to_remove.prev.next = to_remove.next
    to_remove.next.prev = to_remove.prev
    self.__size = self.__size - 1
    return to_remove.value

  def get_element_at(self, index):
    if index >= self.__size or index < 0:
        raise IndexError
    if index < self.__size/2:
        to_get = self.__header.next
        for i in range(index):#go to the element with given index
            to_get = to_get.next
    else:#if the given index is in the second half, start from trailer.
        to_get = self.__trailer.prev
        for i in range(self.__size-1-index):#go to the element with given index
            to_get = to_get.prev
    return to_get.value

  def rotate_left(self):
    if self.__size > 1:#does nothing if linked list is empty or size is one.
        last_element = self.__trailer.prev
        self.__trailer.prev = self.__header.next
        self.__header.next = self.__trailer.prev.next
        self.__header.next.prev = self.__header
        self.__trailer.prev.next = self.__trailer
        self.__trailer.prev.prev = last_element
        self.__trailer.prev.prev.next = self.__trailer.prev


  def __str__(self):
    if self.__size == 0:
        return '[ ]'
    to_return = '['
    cur = self.__header.next
    for index in range (0, self.__size-1):
        to_return += ' ' + str(cur.value) + ','
        cur = cur.next
    to_return += ' ' + str(cur.value) + ' ]'
    return to_return


  def __iter__(self):
    self.to_fetch = self.__header
    return self

  def __next__(self):
    if self.to_fetch.next == self.__trailer:
        raise StopIteration
    self.to_fetch = self.to_fetch.next
    return self.to_fetch.value

if __name__ == '__main__':
  test = Linked_List()
  print("tests if __str__ works when linked list is empty.")
  print(str(test))
  test.append_element(13)#Test if size and content of an empty linked list change after appending an element. Also testes if append_element works when linked list is empty.
  print(str(test))
  test.append_element(1)
  print(str(test))
