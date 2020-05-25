import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  def test_empty_LL_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')

  def test_empty_LL_deque_push_front(self):
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_empty_LL_deque_push_back(self):
    self.__deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_empty_LL_deque_pop_front_return(self):#tests if pop method returns correctly, should return None.
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)

  def test_empty_LL_deque_pop_back_return(self):
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)

  def test_empty_LL_deque_pop_front(self):#tests if pop method works correctly when the deque is empty.
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_LL_deque_pop_back(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_LL_deque_peek_front(self):
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)

  def test_empty_LL_deque_peek_back(self):
    returned = self.__deque.peek_back()
    self.assertEqual(None, returned)

  def test_empty_LL_deque_len(self):
    self.assertEqual(0, len(self.__deque))


  def test_one_LL_deque_string(self):#same testing for a deque of size 1.
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_one_LL_deque_push_front(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_one_LL_deque_push_back(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_one_LL_deque_pop_front_return(self):#tests if pop method returns correctly.
    self.__deque.push_front(1)
    returned = self.__deque.pop_front()
    self.assertEqual(1, returned)

  def test_one_LL_deque_pop_back_return(self):
    self.__deque.push_front(1)
    returned = self.__deque.pop_back()
    self.assertEqual(1, returned)

  def test_one_LL_deque_pop_front(self):#tests if pop method removes correctly.
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_one_LL_deque_pop_back(self):
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_one_LL_deque_peek_front(self):
    self.__deque.push_front(1)
    returned = self.__deque.peek_front()
    self.assertEqual(1, returned)

  def test_one_LL_deque_peek_back(self):
    self.__deque.push_front(1)
    returned = self.__deque.peek_back()
    self.assertEqual(1, returned)

  def test_one_LL_deque_len(self):
    self.__deque.push_front(1)
    self.assertEqual(1, len(self.__deque))

  def test_two_LL_deque_string(self):#same tests for a deque with size 2.
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_two_LL_deque_push_front(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

  def test_two_LL_deque_push_back(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_two_LL_deque_pop_front_return(self):#tests if pop method returns correctly.
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.pop_front()
    self.assertEqual(2, returned)

  def test_two_LL_deque_pop_back_return(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.pop_back()
    self.assertEqual(1, returned)

  def test_two_LL_deque_pop_front(self):#tests if pop method removes correctly.
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_two_LL_deque_pop_back(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.assertEqual('[ 2 ]', str(self.__deque))

  def test_two_LL_deque_peek_front(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.peek_front()
    self.assertEqual(2, returned)

  def test_two_LL_deque_peek_back(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.peek_back()
    self.assertEqual(1, returned)

  def test_two_LL_deque_len(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(2, len(self.__deque))

  def test_LL_deque_push_pop(self):#test if multiple push and pop work correctly
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_back(2)
    self.__deque.pop_back()
    self.__deque.push_front(3)
    self.__deque.pop_front()
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_empty_ARR_deque_string(self):
    self.__deque = get_deque(1)
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')

  def test_empty_ARR_deque_push_front(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_empty_ARR_deque_push_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_empty_ARR_deque_pop_front_return(self):#tests if pop method returns correctly, should return None.
    self.__deque = get_deque(1)
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)

  def test_empty_ARR_deque_pop_back_return(self):
    self.__deque = get_deque(1)
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)

  def test_empty_ARR_deque_pop_front(self):#tests if pop method works correctly when the deque is empty.
    self.__deque = get_deque(1)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_ARR_deque_pop_back(self):
    self.__deque = get_deque(1)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_ARR_deque_peek_front(self):
    self.__deque = get_deque(1)
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)

  def test_empty_ARR_deque_peek_back(self):
    self.__deque = get_deque(1)
    returned = self.__deque.peek_back()
    self.assertEqual(None, returned)

  def test_empty_ARR_deque_len(self):
    self.__deque = get_deque(1)
    self.assertEqual(0, len(self.__deque))


  def test_one_ARR_deque_string(self):#same testing for a deque of size 1.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_one_ARR_deque_push_front(self):#also tests if __grow works
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_one_ARR_deque_push_back(self):#also tests if __grow works
    self.__deque = get_deque(1)
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_one_ARR_deque_pop_front_return(self):#tests if pop method returns correctly.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    returned = self.__deque.pop_front()
    self.assertEqual(1, returned)

  def test_one_ARR_deque_pop_back_return(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    returned = self.__deque.pop_back()
    self.assertEqual(1, returned)

  def test_one_ARR_deque_pop_front(self):#tests if pop method removes correctly.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_one_ARR_deque_pop_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_one_ARR_deque_peek_front(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    returned = self.__deque.peek_front()
    self.assertEqual(1, returned)

  def test_one_ARR_deque_peek_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    returned = self.__deque.peek_back()
    self.assertEqual(1, returned)

  def test_one_ARR_deque_len(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.assertEqual(1, len(self.__deque))

  def test_two_ARR_deque_string(self):#same tests for a deque with size 2.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_two_ARR_deque_push_front(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

  def test_two_ARR_deque_push_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_two_ARR_deque_pop_front_return(self):#tests if pop method returns correctly.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.pop_front()
    self.assertEqual(2, returned)

  def test_two_ARR_deque_pop_back_return(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.pop_back()
    self.assertEqual(1, returned)

  def test_two_ARR_deque_pop_front(self):#tests if pop method removes correctly.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_two_ARR_deque_pop_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.assertEqual('[ 2 ]', str(self.__deque))

  def test_two_ARR_deque_peek_front(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.peek_front()
    self.assertEqual(2, returned)

  def test_two_ARR_deque_peek_back(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    returned = self.__deque.peek_back()
    self.assertEqual(1, returned)

  def test_two_ARR_deque_len(self):
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(2, len(self.__deque))

  def test_ARR_deque_push_pop(self):#test if multiple push and pops work expectedly
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_back(2)
    self.__deque.pop_back()
    self.__deque.push_front(3)
    self.__deque.pop_front()
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_ARR_deque_push_front_circularity(self):#tests push_front when front index is 0.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

  def test_ARR_deque_push_back_circularity(self):#similarly,tests if circular array works
    self.__deque = get_deque(1)
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_ARR_deque_pop_front_circularity(self):#tests pop_front when front index is capacity-1.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_ARR_deque_pop_back_circularity(self):#tests pop_back when back index is 0.
    self.__deque = get_deque(1)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.assertEqual('[ 2 ]', str(self.__deque))

  def test_empty_stack_str(self):
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_len(self):
    self.assertEqual(0, len(self.__stack))

  def test_empty_stack_push(self):
    self.__stack.push(1)
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_empty_stack_pop_return(self):#tests if pop returns value correctly
    self.assertEqual(None, self.__stack.pop())

  def test_empty_stack_pop_remove(self):#tests if pop removes value correctly
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_peek(self):
    self.assertEqual(None, self.__stack.peek())

  def test_one_stack_str(self):
    self.__stack.push(1)
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_one_stack_len(self):
    self.__stack.push(1)
    self.assertEqual(1, len(self.__stack))

  def test_one_stack_push(self):#notice that the top of stack is the at back of the deque, so the printed string from left to right is from bottom to top.
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual('[ 1, 2 ]', str(self.__stack))

  def test_one_stack_pop_return(self):#tests if pop returns value correctly
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_one_stack_pop_remove(self):#tests if pop removes value correctly
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_one_stack_peek(self):
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.peek())

  def test_two_stack_str(self):#notice that the top of stack is the at back of the deque
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual('[ 1, 2 ]', str(self.__stack))

  def test_two_stack_len(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(2, len(self.__stack))

  def test_two_stack_push(self):#notice that the top of stack is the at back of the deque
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))

  def test_two_stack_pop_return(self):#tests if pop returns value correctly
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(2, self.__stack.pop())

  def test_two_stack_pop_remove(self):#tests if pop removes value correctly
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_two_stack_peek(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(2, self.__stack.peek())

  def test_stack_multiple_push_pop(self):#test if multiple push and pops work as expected
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.push(4)
    self.__stack.pop()
    self.__stack.push(6)
    self.__stack.push(7)
    self.__stack.push(8)
    self.__stack.pop()
    self.assertEqual('[ 1, 6, 7 ]', str(self.__stack))

  def test_empty_queue_str(self):
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_queue_len(self):
    self.assertEqual(0, len(self.__queue))

  def test_empty_queue_enqueue(self):
    self.__queue.enqueue(1)
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_empty_queue_dequeue_return(self):#tests if dequeue returns value correctly
    self.assertEqual(None, self.__queue.dequeue())

  def test_empty_queue_dequeue_remove(self):#tests if dequeue removes value correctly
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_queue_peek(self):
    self.assertEqual(None, self.__queue.peek())

  def test_one_queue_str(self):
    self.__queue.enqueue(1)
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_one_queue_len(self):
    self.__queue.enqueue(1)
    self.assertEqual(1, len(self.__queue))

  def test_one_queue_enqueue(self):#notice that the right end of string representation is the back of queue.
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('[ 1, 2 ]', str(self.__queue))

  def test_one_queue_dequeue_return(self):#tests if dequeue returns value correctly
    self.__queue.enqueue(1)
    self.assertEqual(1, self.__queue.dequeue())

  def test_one_queue_dequeue_remove(self):#tests if dequeue removes value correctly
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_one_queue_peek(self):
    self.__queue.enqueue(1)
    self.assertEqual(1, self.__queue.peek())

  def test_two_queue_str(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('[ 1, 2 ]', str(self.__queue))

  def test_two_queue_len(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(2, len(self.__queue))

  def test_two_queue_enqueue(self):#notice that the right end of string representation is the back of queue.
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

  def test_two_queue_dequeue_return(self):#tests if dequeue returns value correctly
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(1, self.__queue.dequeue())

  def test_two_queue_dequeue_remove(self):#tests if dequeue removes value correctly
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ 2 ]', str(self.__queue))

  def test_two_queue_peek(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(1, self.__queue.peek())

  def test_queue_multiple_enqueue_dequeue(self):#test if multiple enqueues and dequeues work as expected
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.enqueue(6)
    self.__queue.enqueue(7)
    self.__queue.enqueue(8)
    self.__queue.dequeue()
    self.assertEqual('[ 6, 7, 8 ]', str(self.__queue))
if __name__ == '__main__':
  unittest.main()
