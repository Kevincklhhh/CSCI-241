from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()


  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def enqueue(self, val):
    self.__dq.push_back(val)

  def dequeue(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
    test = Queue()
    test.enqueue(1)
    print(test)
    test.enqueue(2)
    print(test)
    test.enqueue(3)
    print(test)
    test.dequeue()
    print(test)
    print(test.peek())
#  pass
