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
        raise IndexErrors
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
    toprint = '[ '
    cur = self.__header.next#use cur to walk through all nodes
    for index in range (0, self.__size):
        toprint += str(cur.value)
        if index != self.__size - 1:
            toprint += ', '
        else:
            toprint += ' '
        cur = cur.next
    toprint += ']'
    return toprint


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
  print("tests if __len__ works when linked list is empty.")
  print("Linked list has " + str(len(test)) + " elements.")
  test.append_element(13)#Test if size and content of an empty linked list change after appending an element. Also testes if append_element works when linked list is empty.

  print("tests if __len__ works when linked list is empty.")
  print("Linked list has " + str(len(test)) + " elements.")
  print("tests if __str__ works when linked list has one element.")
  print(str(test))
  print("tests if __len__ works when linked list has one element.")
  print("Linked list has " + str(len(test)) + " elements.")
  test.append_element(2)
  print("tests if __str__ works when linked list has 2 elements.")
  print(str(test))
  print("tests if __len__ works when linked list has 2 elements.")
  print("Linked list has " + str(len(test)) + " elements.")
  test.append_element(-1)#populating array for later testing.
  test.append_element(10)

  print("testing __iter__ ")
  print(str(test))
  for val in test:
      print(val)
  print("testing __iter__ when linked list is empty, nothing is printed below.")
  empty_list = Linked_List()
  for val in empty_list:
      print(val)
  print("testing __iter__ when linked list has one element. 233 should be printed")
  one_element_list = Linked_List()
  one_element_list.append_element(233)
  for val in one_element_list:#should print value of all nodes in the linked list.
      print(val)


  print("testing for insert function starts here.")
  print(str(test))
  print("inserting in the second half of the linked list, insert 233 at index 1. Should work fine.")
  try:#the following one should work fine
      test.insert_element_at(233,1)#inserting in the first half of the linked list
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#size and structure of the linked list are correctly modified.

  print("inserting in the second half of the linked list, insert 333 at index 3. Should work fine.")
  try:#the following one should work fine
      test.insert_element_at(333,3)#inserting in the second half of the linked list
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#size and structure of the linked list are correctly modified.

  print("test a boundary value index, 0. Should work fine.")
  try:#the following one should work fine
      test.insert_element_at(23,0)#inserting at boundary value index.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#size and structure of the linked list are correctly modified.

  print("test a boundary value index, 6. Should work fine.")
  try:#the following one should work fine
      test.insert_element_at(24,6)#inserting at boundary value index.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#size and structure of the linked list are correctly modified.

  print("Test an out-of bound index,-1. Should fail as index is not valid.")
  try:#should fail, index is not valid. The size and contents of linked list does not change.
      test.insert_element_at(233,-1)
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("Test an out-of bound index, 8. Should fail as index is not valid.")
  try:#should fail, insert method cannot be used to append an element, so index is not valid. The size and contents of linked list does not change.
      test.insert_element_at(233,8)
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))
  for i in range (7):#decrease the linked list size to 1.
      test.remove_element_at(0)
  print("linked list size is decreased to 1 for further testing.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("test insert function when linked list size is 1. Should work fine.")
  try:#should work fine.
      test.insert_element_at(2333,0)#Tests if function works properly when linked list size is 1.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))
  test.remove_element_at(0)
  test.remove_element_at(0)#decrease the linked list size to 0.
  print("Linked list size is decreased to 0 for further testing.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("Test insert function when linked list size is 0. Should fail as insert function can not append element. ")
  try:#should fail, insert method cannot be used to append an element, so index is not valid. The size and contents of linked list does not change.
      test.insert_element_at(233,0)
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))


  print("testing for insert function ends here. Below are testings for remove function.")
  test.append_element(13)#populating array for later testing.
  test.append_element(233)
  test.append_element(2)
  test.append_element(-1)
  test.append_element(10)
  print("Remove at index -1, should fail. Index is not valid.")
  try:#should fail. Index is not valid. The size and contents of linked list does not change.
      test.remove_element_at(-1)
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("Remove at index 6, should fail. Index is not valid.")
  try:#should fail. Index is not valid. The size and contents of linked list does not change.
      test.remove_element_at(6)
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements")
  print(str(test))

  print("remove an element from first half, should work fine.")
  try:#the following one should work fine
      print(test.remove_element_at(1))#removing an element in the first half of the linked list. Here 233 is removed and returned.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements")
  print(str(test))#The element at index 1 is removed and returned. Size and structure of the linked list are correctly modified.

  print("remove an element from second half, should work fine.")
  try:#the following one should work fine
      print(test.remove_element_at(2))#removing an element in the second half of the linked list. Here 10 is removed and returned.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#The element at index 3 is removed and returned. Size and structure of the linked list are correctly modified.

  print("removing an element at boundary value. Should work fine.")
  try:#the following one should work fine
      print(test.remove_element_at(0))#removing an element at boundary value. Should work fine.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#The element at index 3 is removed and returned. Size and structure of the linked list are correctly modified.

  print("removing an element at boundary value. Should work fine.")
  try:#the following one should work fine
      print(test.remove_element_at(1))#removing an element at boundary value. Should work fine.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#The element at index 3 is removed and returned. Size and structure of the linked list are correctly modified.

  print("removing an element when the size is 1, should work fine.")
  try:#the following one should work fine
      print(test.remove_element_at(0))#removing an element when the size is 1. Here 10 is removed and returned.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#The element at index 3 is removed and returned. Size and structure of the linked list are correctly modified.

  print("removing an element when the size is 0, should fail.")
  try:#Tests if remove function works when size is 0. Should fail as index is out of range.
      print(test.remove_element_at(0))#removing an element in the second half of the linked list. Here 10 is removed and returned.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))#The element at index 3 is removed and returned. Size and structure of the linked list are correctly modified.

  print("testing for remove function ends here. Below are testings for get function.")

  test.append_element(13)#populating array for later testing.
  test.append_element(233)
  test.append_element(2)
  test.append_element(-1)
  test.append_element(10)
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))
  print("testing get element from first half, should work fine.")
  try:#should work fine. The size and contents of linked list does not change.
      print(test.get_element_at(0))#return the value of element at index 0, which is 13.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element from second half, should work fine.")
  try:#should work fine. The size and contents of linked list does not change.
      print(test.get_element_at(3))#return the value of element at index 3, which is -1.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element at 5, should fail as index is not valid.")
  try:#should fail. Index is not valid. The size and contents of linked list does not change.
      print(test.get_element_at(5))
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element at -1, should fail as index is not valid.")
  try:#should fail. Index is not valid. The size and contents of linked list does not change.
     print(test.get_element_at(-1))
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element at boundary value idex, should work fine")
  try:#should work fine. The size and contents of linked list does not change.
      print(test.get_element_at(4))#return the value of element at index 3, which is -1.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element at boundary value idex, should work fine")
  try:#should work fine. The size and contents of linked list does not change.
      print(test.get_element_at(0))#return the value of element at index 3, which is -1.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  for i in range (4):#decrease the linked list size to 1.
      test.remove_element_at(0)
  print("Linked list'size is decreased to 1 for further testing")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element when linked list size is 1, should work fine")
  try:#should work fine. The size and contents of linked list does not change.
      print(test.get_element_at(0))#Tests if the function works properly when linked list size is 1. Return the value of element at index 0.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))


  test.remove_element_at(0)
  print("Linked list'size is decreased to 0 for further testing")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  print("testing get element when linked list size is 0, should fail as index is out of bound.")
  try:#should fail. Index is invalid for an empty linked list.
      print(test.get_element_at(0))#Tests if the function works properly when linked list size is 0.
  except IndexError:
      print("Index is not valid.")
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))
  print("testing for get function ends here. Below are testings for rotate_left function.")

  test.append_element(10)#populating array for later testing.
  test.append_element(13)
  test.append_element(233)
  test.append_element(2)
  test.append_element(-1)
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))
  test.rotate_left()#All elements should be shifted to the position with index-1. The elements at index 0 is now at index size-1.
  print("Linked list has " + str(len(test)) + " elements.")#Size should be unchanged.
  print(str(test))

  test.remove_element_at(0)#Removing elements to test rotate_left when linked list has size 2.
  test.remove_element_at(0)
  test.remove_element_at(0)
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))



  test.rotate_left()#The first element should be at the last position. The second one is at the first position.
  print("Linked list has " + str(len(test)) + " elements.")#Size should be unchanged.
  print(str(test))

  test.remove_element_at(0)#Removeing elements to test some functions when linked list has size 1.
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))




  test.rotate_left()#The linked list should be unchanged.
  print("Linked list has " + str(len(test)) + " elements.")#Size should be unchanged.
  print(str(test))

  test.remove_element_at(0)#Removeing elements to test some fuctions when linked list is empty.
  print("Linked list has " + str(len(test)) + " elements.")
  print(str(test))

  test.rotate_left()#Rotate left function should have no effect on the empty linked list.
  print("Linked list has " + str(len(test)) + " elements.")#Size should be unchanged.
  print(str(test))
