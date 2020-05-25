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

  def __returnGivenLevel(self,t,level,to_return):
    if t is None:
        return to_return
    if level == 1:
        to_return.append(t)
        return to_return
    elif level > 1 :
        to_return = self.__returnGivenLevel(t.left_child,level-1,to_return)
        to_return = self.__returnGivenLevel(t.right_child,level-1,to_return)
        return to_return

  def visualize_by_level(self,level,str_repr):
        nodesinlevel = []
        nodesinlevel = self.__returnGivenLevel(self.__root,level,nodesinlevel)
        line1 = ''
        line2 = ''
        if level == self.get_height():
            str_repr = ''
        elif level == self.get_height()-1:
            str_repr = self.visualize_by_level(level+1,str_repr)
            for node in nodesinlevel:
                if node.left_child is not None:
                    node.left_string += (len(str(node.left_child.value)) + len(node.left_child.left_string) + 1 ) * ' '
                    node.left_string += len(node.left_child.right_string) * '_'
                if node.right_child is not None:
                    node.right_string += len(node.right_child.left_string) * '_'
                    node.right_string += (len(str(node.right_child.value)) + len(node.right_child.right_string) + 1 ) * ' '
                line2 += node.left_child.left_string + str(node.left_child.value) + node.left_child.right_string + len(str(node.value))* ' '  + node.right_child.left_string + str(node.right_child.value) + node.right_child.right_string
                line1 += (len(node.left_child.left_string) + len(str(node.left_child.value))) * ' ' + '/' + len(node.left_child.right_string) * ' '
                line1 += len(node.right_child.left_string) * ' ' +  '\\' + len(str(node.right_child.value)) * ' ' + len(node.right_child.right_string) * ' '
        else:
            str_repr = self.visualize_by_level(level+1,str_repr)
            for node in nodesinlevel:
                if node.left_child is not None:
                    node.left_string += (len(str(node.left_child.value)) + len(node.left_child.left_string) + 1 ) * ' '
                    node.left_string += len(node.left_child.right_string) * '_'
                if node.right_child is not None:
                    node.right_string += len(node.right_child.left_string) * '_'
                    node.right_string += (len(str(node.right_child.value)) + len(node.right_child.right_string) + 1 ) * ' '
                line2 += node.left_child.left_string + str(node.left_child.value) + node.left_child.right_string + len(str(node.value))* ' '  + node.right_child.left_string + str(node.right_child.value) + node.right_child.right_string
                line1 += (len(node.left_child.left_string) + len(str(node.left_child.value))) * ' ' + '/' + len(node.left_child.right_string) * ' '
                line1 += len(node.right_child.left_string) * ' ' +  '\\' + len(str(node.right_child.value)) * ' ' + len(node.right_child.right_string) * ' '
        str_repr = line1 + '\n' + line2
        return str_repr

  def __visualize_recursion(self,t):
      line1 = []
      line2 = []
      str_repr = ''
      if t.left_child is None and t.right_child is None:
          line1.append('')
          line1.append(str(t.value))
          line1.append('')
      else:
          line1.append('')
          line2.append('')
          if t.left_child is not None:
              left = self.__visualize_recursion(t.left_child)[2]
              leftline1 = self.__visualize_recursion(t.left_child)[0]
              line1.append((len(leftline1[0]) + len(str(leftline1[1])) + 1 ) * ' ')
              line1[0] += (len(leftline1[1]) * '_')
              line2[0] += ((len(line1[0]) + len(str(t.left_child.value)) + len(leftline1[1])) * ' ')
              line2[0] += '/'
              str_repr += '\n'+''.join(self.__visualize_recursion(t.left_child)[2])
              #print(self.__visualize_recursion(t.left_child)[2])
          line1.append(str(t.value))
          if t.right_child is not None:
              right = self.__visualize_recursion(t.right_child)[2]
              rightline1 = self.__visualize_recursion(t.right_child)[0]
              line1.append(len(rightline1[0]) * '_')#right child's left len of space_
              line1[2] += ((len(rightline1[1]) + len(str(rightline1[1])) + 1 ) * ' ')
              line2[0] += (len(rightline1[0]) + len(str(t.value))) * ' '
              line2[0] += '\\'
              #print(self.__visualize_recursion(t.right_child)[1])
              str_repr += '\n' + ''.join(self.__visualize_recursion(t.right_child)[2])
      str_repr = ''.join(line1) +'\n' + ''.join(line2) +'\n' + str_repr
#left child's right len of space_
      return line1, line2, str_repr


  def visualize1(self):
      return self.__visualize_recursion(self.__root)[2]
  '''
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
  '''



if __name__ == '__main__':
    test = Binary_Search_Tree()
    test.insert_element(0)
    test.insert_element(-4)
    test.insert_element(4)
    test.insert_element(-8)
    test.insert_element(8)
    test.insert_element(-2)
    test.insert_element(2)
    test.insert_element(16)
    test.insert_element(-6)
    test.insert_element(6)
    test.insert_element(-16)
    test.insert_element(-3)
    test.insert_element(-1)
    test.insert_element(3)
    test.insert_element(1)
    print(test.visualize_by_level(1,''))
    print(test.visualize_by_level(2,''))
    print(test.visualize_by_level(3,''))
