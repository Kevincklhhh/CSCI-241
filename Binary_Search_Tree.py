class Binary_Search_Tree:


  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left_child = None
      self.right_child = None
      self.height = 0


  def __init__(self):
    self.__root = None
    self.__to_list_index = 0#used in to_list

  def __get_node_height(self,t):#private method used to get height of a node.
      if t is None:
          return 0
      elif t.left_child is None and t.right_child is None:#update the t's height based on height of its child nodes.
          return 1
      elif t.right_child is None:
          return t.left_child.height + 1
      elif t.left_child is None:
          return t.right_child.height + 1
      else:
          return max(t.right_child.height,t.left_child.height) + 1

  def __get_balance(self,t):#return balance factor of a node
      if t is None:
          return 0
      else:
          return self.__get_node_height(t.right_child) - self.__get_node_height(t.left_child)

  def __rightrotate(self,t):#private method, right rotate node t
      new_root = t.left_child
      t.left_child = new_root.right_child
      new_root.right_child = t
      t.height = self.__get_node_height(t)
      new_root.height = self.__get_node_height(new_root)
      return new_root

  def __leftrotate(self,t):#private method, left rotate node t
      new_root = t.right_child
      t.right_child = new_root.left_child
      new_root.left_child = t
      t.height = self.__get_node_height(t)
      new_root.height = self.__get_node_height(new_root)
      return new_root

  def __balance(self,t):
      if t is None:
          return t
      if self.__get_balance(t) == -2:
          print("rotate")
          if self.__get_balance(t.left_child) == -1 or self.__get_balance(t.left_child) == 0:
              t = self.__rightrotate(t)
              return t
          elif self.__get_balance(t.left_child) == 1:#needs double rotation
              t.left_child = self.__leftrotate(t.left_child)
              t = self.__rightrotate(t)
              return t
      if self.__get_balance(t) == 2:
          print("rotate")
          if self.__get_balance(t.right_child) == 1 or self.__get_balance(t.right_child) == 0:
              t = self.__leftrotate(t)
              return t
          elif self.__get_balance(t.right_child) == -1:#needs double rotation
              t.right_child = self.__rightrotate(t.right_child)
              t = self.__leftrotate(t)
              return t
      else:
          return t


  def __recursion_insert(self,t,value):
      if t is None:
          t = self.__BST_Node(value)
          t.height = 1
          return t #return it without checking its balance.
      elif t.value == value:
          raise ValueError
      elif t.value < value:
          t.right_child = self.__recursion_insert(t.right_child,value)
      elif t.value > value:
          t.left_child = self.__recursion_insert(t.left_child,value)
      t.height = self.__get_node_height(t)
      return self.__balance(t)



  def insert_element(self, value):
      self.__root = self.__recursion_insert(self.__root,value)



  def __recursion_remove(self,t,value):
      if t is None:
          raise ValueError
      elif t.value == value:
          if t.right_child is None and t.left_child is None:#no child
              return None
          elif t.left_child is not None and t.right_child is not None:#two children
              min = t.right_child
              while min.left_child is not None:#find the minimum value in the subtree rooted at t's right child
                  min = min.left_child
              t.value = min.value
              t.right_child = self.__recursion_remove(t.right_child,min.value)
          elif t.right_child is not None:#One child
              return t.right_child
          elif t.left_child is not None:
              return t.left_child
      elif value < t.value:
          t.left_child = self.__recursion_remove(t.left_child,value)
      elif value > t.value:
          t.right_child = self.__recursion_remove(t.right_child,value)
      t.height = self.__get_node_height(t)
      return self.__balance(t)

  def remove_element(self, value):
      self.__root = self.__recursion_remove(self.__root,value)

  def __list_recursion(self,t,to_return):#the private recursion method for to_list
      if t is None:
          return to_return
      else:
          to_return = self.__list_recursion(t.left_child,to_return)
          to_return[self.__to_list_index] = t.value
          self.__to_list_index += 1
          to_return = self.__list_recursion(t.right_child,to_return)
      return to_return

  def __count_node_number(self,t,to_return):#return number of nodes in the tree, used in to_list when createing an empty list
      if t is None:
          return to_return#to_return is a counter used to count number of nodes
      else:
          to_return = self.__count_node_number(t.left_child,to_return)
          to_return += 1
          to_return = self.__count_node_number(t.right_child,to_return)
      return to_return

  def to_list(self):
      list_representation = [None] * self.__count_node_number(self.__root,0)#create an empyt list of size = number of nodes
      self.__to_list_index = 0#use this instance attribute to increase one index after adding a node to the list
      return self.__list_recursion(self.__root,list_representation)

  def __in_order_traversal(self,t,to_return):#private recursion method for in_order()
        if t is None:
            return to_return
        else:
            to_return = self.__in_order_traversal(t.left_child,to_return)
            to_return += " " + str(t.value) + ","
            to_return = self.__in_order_traversal(t.right_child,to_return)
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


  def __pre_order_traversal(self,t,to_return):#private recursion method for pre_order()
        if t is None:
            return to_return
        else:
            to_return += " " + str(t.value) + ","
            to_return = self.__pre_order_traversal(t.left_child,to_return)
            to_return = self.__pre_order_traversal(t.right_child,to_return)
        return to_return

  def pre_order(self):
        if self.__root is None:
            return "[ ]"
        to_return = ''
        to_return += self.__pre_order_traversal(self.__root,to_return)
        to_return = to_return[:len(to_return)-1]
        to_return += ' ]'
        to_return = '[' + to_return
        return to_return

  def __post_order_traversal(self,t,to_return):#private recursion method for post_order()
        if t is None:
            return to_return
        else:
            to_return = self.__post_order_traversal(t.left_child,to_return)
            to_return = self.__post_order_traversal(t.right_child,to_return)
            to_return += " " + str(t.value) + ","
        return to_return

  def post_order(self):
        if self.__root is None:
            return "[ ]"
        to_return = ''
        to_return += self.__post_order_traversal(self.__root,to_return)
        to_return = to_return[:len(to_return)-1]
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
  def _build_tree_string(self,root, curr_index, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            self._build_tree_string(root.left_child, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self._build_tree_string(root.right_child, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions

        return new_box, len(new_box[0]), new_root_start, new_root_end

  def visualize(self):

        lines = self._build_tree_string(self.__root, 0, False, '-')[0]
        print()
        return '\n' + '\n'.join((line.rstrip() for line in lines))

if __name__ == '__main__':
    test = Binary_Search_Tree()
    test.insert_element(68)
    test.insert_element(85)
    test.insert_element(26)
    test.insert_element(15)
    test.insert_element(3)
    test.insert_element(40)
    test.insert_element(90)
    test.insert_element(95)
    test.insert_element(75)
    test.insert_element(7)
    test.insert_element(92)
    test.insert_element(87)
    test.insert_element(79)
    test.insert_element(70)
    test.insert_element(81)
    test.insert_element(18)
    test.insert_element(72)
    print(test.visualize())




    #unit tests make the main section unnecessary.
