#The two methods below are written by Joowani and other contributors. The project is at https://github.com/joowani/binarytree. The codes below are from https://github.com/joowani/binarytree/blob/master/binarytree/__init__.py.
#The visualize methods are very helpful in quizzes and testing cases of projects. To use them, simply copy them into binary search tree implementation.
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
#Below is my attempt on binary search tree visualize. Obviously this is a failure.
'''
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
        else:x
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
