from Linked_List_Deque import Linked_List_Deque
from Array_Deque import Array_Deque

# CHANGE THE DEFAULT PARAMETER BETWEEN TEST RUNS
# TO EXERCISE BOTH DEQUE IMPLEMENTATIONS

LL_DEQUE_TYPE = 0
ARR_DEQUE_TYPE = 1

def get_deque(deque_type=LL_DEQUE_TYPE):
  if deque_type == LL_DEQUE_TYPE:
    return Linked_List_Deque()
  elif deque_type == ARR_DEQUE_TYPE:
    return Array_Deque()
  raise NotImplementedError
