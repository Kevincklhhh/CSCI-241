class Set:
  def __init__(self, capacity):
    # allow enough slots for the specified capacity,
    # but track the actual number of elements separately.
    self.__contents = [None] * capacity
    self.__size = 0

  def contains_element(self, value):
    for i in range(self.__size):
      if self.__contents[i] == value:
        return True
    return False

  def insert_element(self, value):
    # if there isn't room to insert the value,
    # raise an exception
    if self.__size == len(self.__contents):
      raise MemoryError

    # raise an exception if the user tries to insert
    # a value that is already in the set.
    if self.contains_element(value):
      raise ValueError

    # if we decide to insert this value, do so in
    # sorted order to make union and intersection easier
    loc = self.__size
    while loc > 0 and self.__contents[loc-1] > value:
      self.__contents[loc] = self.__contents[loc-1]
      loc = loc - 1
    self.__contents[loc] = value
    self.__size = self.__size + 1

  def remove_element(self, value):
    # find the location of the value
    i = 0
    while i < self.__size:
      if self.__contents[i] == value:
        # terminate the while loop
        break
      i = i + 1

    # raise an exception if the user tries to remove
    # a value not in the set.
    if i == self.__size:
      raise ValueError

    # otherwise, shift all of the greater values left one,
    # destroying the deleted value
    while i + 1 < self.__size:
      self.__contents[i] = self.__contents[i+1]
      i = i + 1

    # we deleted an item and shifted everything else
    # left, so we have to erase the last item
    self.__contents[i] = None

    self.__size = self.__size - 1

  def union(self, other):
    result = Set(self.__size + other.__size)
    i = 0
    j = 0
    k = 0
    # knowing that that the arrays are sorted,
    # we can always grab the lower value and advnace that
    # array's index.
    while i < self.__size and j < other.__size:
      if self.__contents[i] < other.__contents[j]:
        result.insert_element(self.__contents[i])
        i = i + 1
      elif other.__contents[j] < self.__contents[i]:
        result.insert_element(other.__contents[j])
        j = j + 1
      else: # the two cells have equal values
        result.insert_element(self.__contents[i])
        i = i + 1
        j = j + 1
      k = k + 1

    # if the arrays are of different size, grab what remains
    # in the longer one.
    while i < self.__size:
      result.insert_element(self.__contents[i])
      i = i + 1
      k = k + 1

    while j < other.__size:
      result.insert_element(other.__contents[j])
      j = j + 1
      k = k + 1

    return result

  def intersection(self, other):
    result = Set(self.__size + other.__size)
    i = 0
    j = 0
    k = 0
    while i < self.__size and j < other.__size:
      if self.__contents[i] < other.__contents[j]:
        i = i + 1
      elif other.__contents[j] < self.__contents[i]:
        j = j + 1
      else: # only insert if the two values match
        result.insert_element(self.__contents[i])
        i = i + 1
        j = j + 1
      k = k + 1

    return result

  def __str__(self):
    # note that this format is different from project 2.
    if self.__size == 0:
      return '[]'
    return str(self.__contents[0:self.__size])

  def __len__(self):
    return self.__size

  def __iter__(self):
    # Somebody is about to iterate through the set.
    # initialize an index to begin.如果for in rnage再get element的话 会quardtic
    self.__iter_index = 0
    return self

  def __next__(self):
    # if there are no more values left,
    # terminate the iteration. Python does this automatically
    # when it receives the exception generated here.
    if self.__iter_index == self.__size:
      raise StopIteration
    # each time a new value is requested (such as
    # a cycle in a for loop), grab the value, up the
    # index to prepare for the next call, and return
    # the value.
    to_return = self.__contents[self.__iter_index]
    self.__iter_index = self.__iter_index + 1
    return to_return

if __name__ == '__main__':
  a = Set(5)
  print(a)
  print('set has ' + str(len(a)) + ' elements')
  try:
    # these should all work without error
    a.insert_element(3)
    a.insert_element(5)
    a.insert_element(-4)
    a.insert_element(1)
  except MemoryError:
    print('Error: Unexpected out of cells')
  except ValueError:
    print('Error: Unexpected no duplicates allowed')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  try:
    # should fail. 3 is already in the set.
    a.insert_element(3)
  except ValueError:
    print('Correctly caught duplicate value 3 exception. No crash!')
  except MemoryError:
    print('Error: Unexpceted out of Cells')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  try:
    # should work fine.
    a.insert_element(7)
  except MemoryError:
    print('Error: Unexpected out of cells')
  except ValueError:
    print('Error: Unexpected no duplicates allowed')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  try:
    # should fail. set is full.
    a.insert_element(9)
  except ValueError:
    print('Error: No duplicates allowed.')
  except MemoryError:
    print('Correctly caught out of cells exception for 9. No crash!')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  #Now let's test the iterator:
  print()
  print('testing iterator:')
  for val in a:
    print(val)
  print()

  # Remove each item, checking everything at each step.
  # Ensure that removing from an empty set does not crash.
  try:
    a.remove_element(5)
  except ValueError:
    print('Error: No such value.')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  try:
    a.remove_element(5)
  except ValueError:
    print('Correctly caught no such value exception for second 5.')
  print(a)
  print('set has ' + str(len(a)) + ' elements')

  try:
    a.remove_element(3)
    print(a)
    print('set has ' + str(len(a)) + ' elements')

    a.remove_element(7)
    print(a)
    print('set has ' + str(len(a)) + ' elements')

    a.remove_element(1)
    print(a)
    print('set has ' + str(len(a)) + ' elements')

    a.remove_element(-4)
    print(a)
    print('set has ' + str(len(a)) + ' elements')

    a.remove_element(17)
    print(a)
    print('set has ' + str(len(a)) + ' elements')
  except ValueError:
    print('Error: No such value.')

  r = Set(3)
  try:
    r.insert_element(4)
    r.insert_element(2)
    r.insert_element(8)
  except ValueError:
    print('Error: unexpected no duplicates allowed.')
  except MemoryError:
    print('Error: unexpected out of cells.')

  s = Set(5)
  try:
    s.insert_element(9)
    s.insert_element(4)
    s.insert_element(2)
    s.insert_element(3)
    s.insert_element(1)
  except ValueError:
    print('Error: unexpected no duplicates allowed.')
  except MemoryError:
    print('Error: unexpected out of cells.')

  print(r)
  print(s)

  print('intersection: ' + str(r.intersection(s)))

  print('union: ' + str(r.union(s)))

  e1 = Set(0)
  e2 = Set(3)

  print('intersection of empty sets: ' + str(e1.intersection(e2)))
  print('union of empty sets: ' + str(e1.union(e2)))
