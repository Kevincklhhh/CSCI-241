from abc import ABCMeta, abstractmethod

# DO NOT CHANGE ANYTHING IN THIS FILE
# (but look into what these things mean)

class Deque(metaclass=ABCMeta):

  @classmethod
  def __subclasshook__(child):
    print('here')
    required_methods = {'push_front', 'push_back', 'peek_front', 'peek_back', 'pop_front', 'pop_back'}
    if required_methods <= child.__dict__.keys():
      return True
    return False

  @abstractmethod
  def __str__(self):
    raise NotImplementedError

  @abstractmethod
  def __len__(self):
    raise NotImplementedError

  @abstractmethod
  def push_front(self, val):
    raise NotImplementedError
  
  @abstractmethod
  def pop_front(self):
    raise NotImplementedError

  @abstractmethod
  def peek_front(self):
    raise NotImplementedError

  @abstractmethod
  def push_back(self, val):
    raise NotImplementedError
  
  @abstractmethod
  def pop_back(self):
    raise NotImplementedError

  @abstractmethod
  def peek_back(self):
    raise NotImplementedError

# DO NOT CHANGE ANYTHING IN THIS FILE
