from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()


  def __str__(self):#notice that the open end of stack is the at back of the deque.
    # TODO replace pass with your implementation.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def push(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_back(val)

  def pop(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_back()

  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_back()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
