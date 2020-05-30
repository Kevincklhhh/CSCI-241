class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.left_child = None
      self.right_child = None
      self.height = 0
      self.left_string = ''#used in visualization
      self.right_string = ''
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def __recursion_insert(self,cur_node,value):
      if cur_node is None:
          cur_node = self.__BST_Node(value)
      elif cur_node.value == value:
          raise ValueError
      elif cur_node.value < value:
          cur_node.right_child = self.__recursion_insert(cur_node.right_child,value)
      elif cur_node.value > value:
          cur_node.left_child = self.__recursion_insert(cur_node.left_child,value)

      if cur_node.left_child is None and cur_node.right_child is None:#update the cur_node's height based on height of its child nodes.
          cur_node.height = 1
      elif cur_node.right_child is None:
          cur_node.height = cur_node.left_child.height + 1
      elif cur_node.left_child is None:
          cur_node.height = cur_node.right_child.height + 1
      else:
          cur_node.height = max(cur_node.right_child.height,cur_node.left_child.height) + 1

      return cur_node



  def insert_element(self, value):
      self.__root = self.__recursion_insert(self.__root,value)



  def __recursion_remove(self,cur_node,value):
      if cur_node is None:
          raise ValueError
      elif cur_node.value == value:
          if cur_node.right_child is None and cur_node.left_child is None:#no child
              return None
          elif cur_node.left_child is not None and cur_node.right_child is not None:#two children
              min = cur_node.right_child
              while min.left_child is not None:#find the minimum value in the subtree rooted at cur_node's right child
                  min = min.left_child
              cur_node.value = min.value
              cur_node.right_child = self.__recursion_remove(cur_node.right_child,min.value)
          elif cur_node.right_child is not None:#One children
              return cur_node.right_child
          elif cur_node.left_child is not None:
              return cur_node.left_child
      elif value < cur_node.value:
          cur_node.left_child = self.__recursion_remove(cur_node.left_child,value)
      elif value > cur_node.value:
          cur_node.right_child = self.__recursion_remove(cur_node.right_child,value)

      if cur_node.left_child is None and cur_node.right_child is None:#update height of cur_node, same code as in insertion private method
          cur_node.height = 1
      elif cur_node.right_child is None:
          cur_node.height = cur_node.left_child.height + 1
      elif cur_node.left_child is None:
          cur_node.height = cur_node.right_child.height + 1
      else:
          cur_node.height = max(cur_node.right_child.height,cur_node.left_child.height) + 1
      return cur_node

  def remove_element(self, value):
      self.__root = self.__recursion_remove(self.__root,value)


  def __in_order_traversal(self,cur_node,to_return):#private recursion method for in_order()
        if cur_node == None:
            return to_return
        else:
            to_return = self.__in_order_traversal(cur_node.left_child,to_return)
            to_return += " " + str(cur_node.value) + ","
            to_return = self.__in_order_traversal(cur_node.right_child,to_return)
        return to_return

  def in_order(self):
        if self.__root is None:
            return "[ ]"
        to_return = ''
        to_return += self.__in_order_traversal(self.__root,to_return)
        to_return = to_return[:len(to_return)-1]
        to_return += ' ]'
        to_return = '[' + to_return
        return to_return


  def __pre_order_traversal(self,cur_node,to_return):#private recursion method for pre_order()
        if cur_node == None:
            return to_return
        else:
            to_return += " " + str(cur_node.value) + ","
            to_return = self.__pre_order_traversal(cur_node.left_child,to_return)
            to_return = self.__pre_order_traversal(cur_node.right_child,to_return)
        return to_return

  def pre_order(self):
        if self.__root is None:
            return "[ ]"
        to_return = ''
        to_return += self.__pre_order_traversal(self.__root,to_return)
        to_return = to_return[:-1]
        to_return += ' ]'
        to_return = '[' + to_return
        return to_return

  def __post_order_traversal(self,cur_node,to_return):#private recursion method for post_order()
        if cur_node == None:
            return to_return
        else:
            to_return = self.__post_order_traversal(cur_node.left_child,to_return)
            to_return = self.__post_order_traversal(cur_node.right_child,to_return)
            to_return += " " + str(cur_node.value) + ","
        return to_return

  def post_order(self):
        if self.__root is None:
            return "[ ]"
        to_return = ''
        to_return += self.__post_order_traversal(self.__root,to_return)
        to_return = to_return[:-1]
        to_return += ' ]'
        to_return = '[' + to_return
        return to_return


  def get_height(self):
      if self.__root is None:
          return 0
      else:
          return self.__root.height


  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
    test = Binary_Search_Tree()
