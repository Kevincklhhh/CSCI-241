from Linked_List import Linked_List

def Josephus(ll):
  # solve the Josephus problem following the following algorithm:
  # rotate the list to the left by one position circularly,
  # and then delete the first element;
  # repeat it until there is only one element left in the list.
  # print the sequence of survivors after each death,
  # and finally print the survivor’s number.
  # TODO replace pass with your implementation
  while len(ll) > 1:
      ll.rotate_left()
      ll.remove_element_at(0)
      print(ll)
  print("The survivor is: "+str(ll.get_element_at(0)))

if __name__ == '__main__':
  n = int(input("Input the total number of people: "))
  ll = Linked_List()
  for i in range(n):
      ll.append_element(i+1)
  # create a new doubly linked list object called ll
  # with n elements named 1 to n.
  # TODO insert your implementation before the print statement
  print("Initial order:", ll)
  Josephus(ll)
