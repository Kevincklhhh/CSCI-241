import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
  def setUp(self):
    self.__test_tree = Binary_Search_Tree()
#below are modified test cases from project 4. They intend to test the three traversals and basic functonalities of insert and remove.
  def test_in_order_empty(self):#tests in order traversal of an empty tree
    self.assertEqual('[ ]', self.__test_tree.in_order())

  def test_in_order_height_one(self):#tests in order traversal of a tree of height 1
    self.__test_tree.insert_element(1)
    self.assertEqual('[ 1 ]', self.__test_tree.in_order())

  def test_in_order_height_two(self):#tests in order traversal of a tree of height 2
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ 0, 1, 2 ]', str(self.__test_tree.in_order()))

  def test_in_order_height_three(self):#tests in order traversal of a tree of height 3
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.assertEqual('[ -2, -1, 0, 1, 2, 3, 4 ]', str(self.__test_tree.in_order()))


  def test_pre_order_empty(self):#tests pre order traversal of an empty tree
    self.assertEqual('[ ]', self.__test_tree.pre_order())

  def test_pre_order_height_one(self):#tests pre order traversal of a tree of height 1
    self.__test_tree.insert_element(1)
    self.assertEqual('[ 1 ]', self.__test_tree.pre_order())

  def test_pre_order_height_two(self):#tests pre order traversal of a tree of height 2
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ 1, 0, 2 ]', str(self.__test_tree.pre_order()))

  def test_pre_order_height_three(self):#tests pre order traversal of a tree of height 3
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.assertEqual('[ 1, -1, -2, 0, 3, 2, 4 ]', str(self.__test_tree.pre_order()))


  def test_post_order_empty(self):#tests post order traversal of an empty tree
    self.assertEqual('[ ]', self.__test_tree.post_order())

  def test_post_order_height_one(self):#tests post order traversal of a tree of height 1
    self.__test_tree.insert_element(1)
    self.assertEqual('[ 1 ]', self.__test_tree.post_order())

  def test_post_order_height_two(self):#tests post order traversal of a tree of height 2
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ 0, 2, 1 ]', str(self.__test_tree.post_order()))

  def test_post_order_height_three(self):#tests post order traversal of a tree of height 3
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.assertEqual('[ -2, 0, -1, 2, 4, 3, 1 ]', str(self.__test_tree.post_order()))


  def test_insert_base_case(self):#tests inserting at root
    self.__test_tree.insert_element(1)
    self.assertEqual('[ 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1 ]', str(self.__test_tree.post_order()))

  def test_insert_left_one_recursion(self):#test inserting with one recursive call
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.assertEqual('[ -1, 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1, -1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -1, 1 ]', str(self.__test_tree.post_order()))

  def test_insert_right_one_recursion(self):#test inserting with one recursive call
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ 1, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 1, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 2, 1 ]', str(self.__test_tree.post_order()))

  def test_insert_left_left_two_recursion(self):#tests insert element at node with depth 3, should be balanced
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-2)
    self.assertEqual('[ -2, -1, 1 ]', str(self.__test_tree))
    self.assertEqual('[ -1, -2, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 1, -1 ]', str(self.__test_tree.post_order()))

  def test_insert_left_right_two_recursion(self):#should be balanced
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-1)
    self.assertEqual('[ -2, -1, 1 ]', str(self.__test_tree))
    self.assertEqual('[ -1, -2, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 1, -1 ]', str(self.__test_tree.post_order()))

  def test_insert_right_left_two_recursion(self):#should be balanced
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 1, 3 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 3, 2 ]', str(self.__test_tree.post_order()))

  def test_insert_right_right_two_recursion(self):#should be balanced
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 1, 3 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 3, 2 ]', str(self.__test_tree.post_order()))

  def test_insert_value_error_depth_one(self):#tests if insert raises exception correctly when the value to insert is already in tree.
    self.__test_tree.insert_element(1)
    with self.assertRaises(ValueError):
      self.__test_tree.insert_element(1)
    self.assertEqual('[ 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1 ]', str(self.__test_tree.post_order()))

  def test_insert_value_error_depth_two(self):#tests when the existing value has depth 2
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(2)
    with self.assertRaises(ValueError):
      self.__test_tree.insert_element(2)
    self.assertEqual('[ 1, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 1, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 2, 1 ]', str(self.__test_tree.post_order()))

  def test_remove_base_case_zero_child(self):#test removing root node when it has zero child.
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(1)
    self.assertEqual('[ ]', str(self.__test_tree))
    self.assertEqual('[ ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ ]', str(self.__test_tree.post_order()))

  def test_remove_base_case_one_child(self):#test removing root node when it has one child.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(1)
    self.assertEqual('[ 2 ]', str(self.__test_tree))
    self.assertEqual('[ 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 2 ]', str(self.__test_tree.post_order()))

  def test_remove_base_case_two_children(self):#test removing root node when it has two children.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(1)
    self.assertEqual('[ 0, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 0 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 0, 2 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_left_zero_child(self):#test removing left child of the root node when it has zero child.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.remove_element(-1)
    self.assertEqual('[ 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_left_one_child(self):#test removing left child of the root node when it has one child.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(0)
    self.__test_tree.remove_element(-1)
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree))
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 0 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_left_two_children(self):#test removing left child of the root node when it has two children.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(-1)
    self.assertEqual('[ -2, 0, 1 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 1, 0 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_right_zero_child(self):#test removing right child of the root node when it has zero child.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.remove_element(3)
    self.assertEqual('[ 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_right_one_child(self):#test removing right child of the root node when it has one child.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)
    self.__test_tree.remove_element(3)
    self.assertEqual('[ 1, 4 ]', str(self.__test_tree))
    self.assertEqual('[ 4, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 4 ]', str(self.__test_tree.post_order()))

  def test_remove_one_recursion_right_two_children(self):#test removing right child of the root node when it has two children.
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.remove_element(3)
    self.assertEqual('[ 1, 2, 4 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 1, 4 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 4, 2 ]', str(self.__test_tree.post_order()))

  def test_remove_two_children_recursion(self):#When removing a node of two children, tests if finding minimum value and recursion works.
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(6)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(0)
    self.assertEqual('[ -4, 1, 2, 4, 6 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 1, -4, 4, 6 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -4, 1, 6, 4, 2 ]', str(self.__test_tree.post_order()))

  def test_remove_empty_tree(self):#test if remove_element() raises exception correcly when the tree is empty.
    with self.assertRaises(ValueError):
        self.__test_tree.remove_element(-1)
    self.assertEqual('[ ]', str(self.__test_tree))
    self.assertEqual('[ ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ ]', str(self.__test_tree.post_order()))

  def test_remove_exception_tree_height_1(self):#test if remove_element() raises exception correcly when the tree height is 1.
    self.__test_tree.insert_element(0)
    with self.assertRaises(ValueError):
        self.__test_tree.remove_element(-1)
    self.assertEqual('[ 0 ]', str(self.__test_tree))
    self.assertEqual('[ 0 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 0 ]', str(self.__test_tree.post_order()))

  def test_remove_exception_tree_height_2(self):#test if remove_element() raises exception correcly when the tree height is 2.
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    with self.assertRaises(ValueError):
        self.__test_tree.remove_element(-1)
    self.assertEqual('[ -2, 0, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 2, 0 ]', str(self.__test_tree.post_order()))

  def test_get_height_empty_tree(self):#test get_height of an empty tree
    self.assertEqual('[ ]', str(self.__test_tree))
    self.assertEqual('[ ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ ]', str(self.__test_tree.post_order()))
    self.assertEqual(0, self.__test_tree.get_height())

  def test_get_height_one_after_insertion(self):##test if insert_element() updates height if both of the children node is none
    self.__test_tree.insert_element(0)
    self.assertEqual('[ 0 ]', str(self.__test_tree))
    self.assertEqual('[ 0 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(1, self.__test_tree.get_height())

  def test_get_height_one_children_none_after_insertion(self):#test if insert_element() updates height correctly if one of the children node is none
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(1)
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree))
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 1, 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(2, self.__test_tree.get_height())

  def test_get_height_two_equal_height_children_after_insertion(self):#test if insert_element() updates height correctly if a node's two children have equal height
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.assertEqual('[ -2, 0, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 2, 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(2, self.__test_tree.get_height())

  def test_get_height_two_unequal_height_children_after_insertion(self):#test if insert_element() updates height correctly if a node's two children have different height
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(3)
    self.assertEqual('[ -2, 0, 2, 3 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 2, 3 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 3, 2, 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(3, self.__test_tree.get_height())

  def test_get_height_one_node_after_removal(self):##test if remove_element() updates height if both of the children node is none
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(1)#extra step of remove_element(1) removes 1 and updates height of nodes above accordingly.
    self.assertEqual('[ 0 ]', str(self.__test_tree))
    self.assertEqual('[ 0 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(1, self.__test_tree.get_height())

  def test_get_height_one_children_none_after_removal(self):#test if remove_element() updates height correctly if one of the children node is none
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(2)#extra step of remove_element(2) removes 2 and updates height of nodes above accordingly.
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree))
    self.assertEqual('[ 1, 0 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ 0, 1 ]', str(self.__test_tree.post_order()))
    self.assertEqual(2, self.__test_tree.get_height())

  def test_get_height_two_equal_height_children_after_removal(self):#test if remove_element() updates height correctly if a node's two children have equal height
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(3)
    self.__test_tree.remove_element(3)#extra step of remove_element(3) removes 3 and updates height of nodes above accordingly.
    self.assertEqual('[ -2, 0, 2 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 2, 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(2, self.__test_tree.get_height())

  def test_get_height_two_unequal_height_children_after_removal(self):#test if remove_element() updates height correctly if a node's two children have different height
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)
    self.__test_tree.remove_element(4)#extra step of remove_element(4) removes 4 and updates height of nodes above accordingly.
    self.assertEqual('[ -2, 0, 2, 3 ]', str(self.__test_tree))
    self.assertEqual('[ 0, -2, 3, 2 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -2, 2, 3, 0 ]', str(self.__test_tree.post_order()))
    self.assertEqual(3, self.__test_tree.get_height())

  def test_get_height_after_complicated_removal(self):#test if remove_element() updates height correctly after removing a node with two children, which calls another recursive call.
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(6)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(0)
    self.assertEqual('[ -4, 1, 2, 4, 6 ]', str(self.__test_tree))
    self.assertEqual('[ 2, 1, -4, 4, 6 ]', str(self.__test_tree.pre_order()))
    self.assertEqual('[ -4, 1, 6, 4, 2 ]', str(self.__test_tree.post_order()))
    self.assertEqual(3, self.__test_tree.get_height())
#below are new tests in project 5. They are intened to test __balance()
  def test_insert_balance_two_one(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual('[ -2, 0, 1, 2, 3, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ 2, 0, -2, 1, 3, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -2, 1, 0, 4, 3, 2 ]', self.__test_tree.post_order())
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual('[ -4, -3, -2, -1, 0, 2 ]', self.__test_tree.in_order())
    self.assertEqual('[ -2, -3, -4, 0, -1, 2 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, -3, -1, 2, 0, -2 ]', self.__test_tree.post_order())
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_positive_two_negative_one(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual('[ -3, 0, 1, 2, 3, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ 2, 0, -3, 1, 3, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -3, 1, 0, 4, 3, 2 ]', self.__test_tree.post_order())
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_negative_two_positive_one(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual('[ -4, -3, -2, -1, 0, 3 ]', self.__test_tree.in_order())
    self.assertEqual('[ -2, -3, -4, 0, -1, 3 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, -3, -1, 3, 0, -2 ]', self.__test_tree.post_order())
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_two_one_left_child(self):#same tests as above, but at root's left child. single rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual('[ -2, 0, 1, 2, 3, 4, 5, 10, 15 ]', self.__test_tree.in_order())
    self.assertEqual('[ 5, 2, 0, -2, 1, 3, 4, 10, 15 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -2, 1, 0, 4, 3, 2, 15, 10, 5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one_left_child(self):#single rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual('[ -4, -3, -2, -1, 0, 2, 5, 10, 15 ]', self.__test_tree.in_order())
    self.assertEqual('[ 5, -2, -3, -4, 0, -1, 2, 10, 15 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, -3, -1, 2, 0, -2, 15, 10, 5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_positive_two_negative_one_left_child(self):#double rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual('[ -3, 0, 1, 2, 3, 4, 5, 10, 15 ]', self.__test_tree.in_order())
    self.assertEqual('[ 5, 2, 0, -3, 1, 3, 4, 10, 15 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -3, 1, 0, 4, 3, 2, 15, 10, 5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_positive_one_left_child(self):#double rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual('[ -4, -3, -2, -1, 0, 3, 5, 10, 15 ]', self.__test_tree.in_order())
    self.assertEqual('[ 5, -2, -3, -4, 0, -1, 3, 10, 15 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, -3, -1, 3, 0, -2, 15, 10, 5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_two_one_right_child(self):#same tests as above, but at root's right child. single rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual('[ -15, -10, -5, -2, 0, 1, 2, 3, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ -5, -10, -15, 2, 0, -2, 1, 3, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -15, -10, -2, 1, 0, 4, 3, 2, -5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one_right_child(self):#single rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual('[ -15, -10, -5, -4, -3, -2, -1, 0, 2 ]', self.__test_tree.in_order())
    self.assertEqual('[ -5, -10, -15, -2, -3, -4, 0, -1, 2 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -15, -10, -4, -3, -1, 2, 0, -2, -5 ]', self.__test_tree.post_order())

  def test_insert_balance_positive_two_negative_one_right_child(self):#double rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual('[ -15, -10, -5, -3, 0, 1, 2, 3, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ -5, -10, -15, 2, 0, -3, 1, 3, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -15, -10, -3, 1, 0, 4, 3, 2, -5 ]', self.__test_tree.post_order())

  def test_insert_balance_negative_two_positive_one_right_child(self):#double rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual('[ -15, -10, -5, -4, -3, -2, -1, 0, 3 ]', self.__test_tree.in_order())
    self.assertEqual('[ -5, -10, -15, -2, -3, -4, 0, -1, 3 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -15, -10, -4, -3, -1, 3, 0, -2, -5 ]', self.__test_tree.post_order())
    self.assertEqual(4,self.__test_tree.get_height())

  def test_remove_balance_two_one(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual('[ 0, 4, 8 ]', self.__test_tree.in_order())
    self.assertEqual('[ 4, 0, 8 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 0, 8, 4 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_negative_one(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -8, -4, 0 ]', self.__test_tree.in_order())
    self.assertEqual('[ -4, -8, 0 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -8, 0, -4 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_negative_one(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual('[ 0, 2, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ 2, 0, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 0, 4, 2 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_positive_one(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -4, -2, 0 ]', self.__test_tree.in_order())
    self.assertEqual('[ -2, -4, 0 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, 0, -2 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_zero(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual('[ 2, 3, 4, 5 ]', self.__test_tree.in_order())
    self.assertEqual('[ 4, 2, 3, 5 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 3, 2, 5, 4 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_zero(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual('[ -2, 0, 1, 2 ]', self.__test_tree.in_order())
    self.assertEqual('[ 0, -2, 2, 1 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -2, 1, 2, 0 ]', self.__test_tree.post_order())

  def test_remove_balance_two_one_left_child(self):#same tests as above, but on root's left child. single rotation
    self.__test_tree.insert_element(9)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual('[ 0, 4, 8, 9, 16, 20 ]', self.__test_tree.in_order())
    self.assertEqual('[ 9, 4, 0, 8, 16, 20 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 0, 8, 4, 20, 16, 9 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_negative_one_left_child(self):#single rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -8, -4, 0, 8, 16, 20 ]', self.__test_tree.in_order())
    self.assertEqual('[ 8, -4, -8, 0, 16, 20 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -8, 0, -4, 20, 16, 8 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_negative_one_left_child(self):#+2-1double rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual('[ 0, 2, 4, 8, 16, 20 ]', self.__test_tree.in_order())
    self.assertEqual('[ 8, 2, 0, 4, 16, 20 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 0, 4, 2, 20, 16, 8 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_positive_one_left_child(self):# double rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -4, -2, 0, 8, 16, 20 ]', self.__test_tree.in_order())
    self.assertEqual('[ 8, -2, -4, 0, 16, 20 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -4, 0, -2, 20, 16, 8 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_zero_left_child(self):# single rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual('[ 2, 3, 4, 5, 8, 16, 20 ]', self.__test_tree.in_order())
    self.assertEqual('[ 8, 4, 2, 3, 5, 16, 20 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 3, 2, 5, 4, 20, 16, 8 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_zero_left_child(self):#single rotation
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual('[ -2, 0, 1, 2, 4, 8, 16 ]', self.__test_tree.in_order())
    self.assertEqual('[ 4, 0, -2, 2, 1, 8, 16 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -2, 1, 2, 0, 16, 8, 4 ]', self.__test_tree.post_order())

  def test_remove_balance_two_one_right_child(self):#Same tests on root's right child. single rotation
    self.__test_tree.insert_element(-8)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)
    self.assertEqual('[ -20, -16, -8, 0, 4, 8 ]', self.__test_tree.in_order())
    self.assertEqual('[ -8, -16, -20, 4, 0, 8 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -20, -16, 0, 8, 4, -8 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_negative_one_right_child(self):#single rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -20, -16, -9, -8, -4, 0 ]', self.__test_tree.in_order())
    self.assertEqual('[ -9, -16, -20, -4, -8, 0 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -20, -16, -8, 0, -4, -9 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_negative_one_right_child(self):#double rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual('[ -20, -16, -9, 0, 2, 4 ]', self.__test_tree.in_order())
    self.assertEqual('[ -9, -16, -20, 2, 0, 4 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -20, -16, 0, 4, 2, -9 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_positive_one_right_child(self):#double rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual('[ -20, -16, -9, -4, -2, 0 ]', self.__test_tree.in_order())
    self.assertEqual('[ -9, -16, -20, -2, -4, 0 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -20, -16, -4, 0, -2, -9 ]', self.__test_tree.post_order())

  def test_remove_balance_positive_two_zero_right_child(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual('[ 2, 3, 4, 5 ]', self.__test_tree.in_order())
    self.assertEqual('[ 4, 2, 3, 5 ]', self.__test_tree.pre_order())
    self.assertEqual('[ 3, 2, 5, 4 ]', self.__test_tree.post_order())

  def test_remove_balance_negative_two_zero_right_child(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual('[ -2, 0, 1, 2 ]', self.__test_tree.in_order())
    self.assertEqual('[ 0, -2, 2, 1 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -2, 1, 2, 0 ]', self.__test_tree.post_order())

  def test_remove_multiple_balance(self):#A tree that needs multiple balance after removing a node
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(-24)
    self.__test_tree.insert_element(-8)
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(24)
    self.__test_tree.insert_element(-28)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(12)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(28)
    self.__test_tree.insert_element(-30)
    self.__test_tree.insert_element(6)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(14)
    self.__test_tree.insert_element(30)
    self.__test_tree.insert_element(15)
    self.__test_tree.remove_element(20)
    self.assertEqual('[ -30, -28, -24, -20, -16, -8, -4, 0, 4, 6, 8, 10, 12, 14, 15, 16, 24, 28, 30 ]', self.__test_tree.in_order())
    self.assertEqual('[ 0, -16, -24, -28, -30, -20, -8, -4, 12, 8, 4, 6, 10, 16, 14, 15, 28, 24, 30 ]', self.__test_tree.pre_order())
    self.assertEqual('[ -30, -28, -20, -24, -4, -8, -16, 6, 4, 10, 8, 15, 14, 24, 30, 28, 16, 12, 0 ]', self.__test_tree.post_order())

  def test_insert_balance_two_one_height(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one_height(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_positive_two_negative_one_height(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_negative_two_positive_one_height(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual(3,self.__test_tree.get_height())

  def test_insert_balance_two_one_left_child_height(self):#same tests as above, but at root's left child
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one_left_child_height(self):#single rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_positive_two_negative_one_left_child_height(self):#double rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_positive_one_left_child_height(self):#double rotation
    self.__test_tree.insert_element(5)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_two_one_right_child_height(self):#same tests as above, but at root's right child,single rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(4)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_insert_balance_negative_two_negative_one_right_child_height(self):#single rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(-4)#needs balance
    self.assertEqual(4, self.__test_tree.get_height())

  def test_insert_balance_positive_two_negative_one_right_child_height(self):#double rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(1)#needs balance
    self.assertEqual(4, self.__test_tree.get_height())

  def test_insert_balance_negative_two_positive_one_right_child_height(self):#double rotation
    self.__test_tree.insert_element(-5)
    self.__test_tree.insert_element(-10)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-15)
    self.__test_tree.insert_element(-3)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(-1)#needs balance
    self.assertEqual(4,self.__test_tree.get_height())

  def test_remove_balance_two_one_height(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(2, self.__test_tree.get_height())

  def test_remove_balance_negative_two_negative_one_height(self):#single rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(2, self.__test_tree.get_height())

  def test_remove_balance_positive_two_negative_one_height(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(2, self.__test_tree.get_height())

  def test_remove_balance_negative_two_positive_one_height(self):#double rotation
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(2, self.__test_tree.get_height())

  def test_remove_balance_positive_two_zero_height(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_zero_height(self):#single rotation
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_two_one_left_child_height(self):#same tests as above, but on root's left child.+2+1single rotation
    self.__test_tree.insert_element(9)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_negative_one_left_child_height(self):#-2-1single rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_positive_two_negative_one_left_child_height(self):#+2-1double rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_positive_one_left_child_height(self):#-2+1 double rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_positive_two_zero_left_child_height(self):#2 0 single rotation
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual(4, self.__test_tree.get_height())

  def test_remove_balance_negative_two_zero_left_child_height(self):#-2 0 single rotation
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual(4, self.__test_tree.get_height())

  def test_remove_balance_two_one_right_child_height(self):#Same tests on root's right child. single rotation
    self.__test_tree.insert_element(-8)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(8)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_negative_one_right_child_height(self):#single rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-8)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_positive_two_negative_one_right_child_height(self):#double rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(2)
    self.__test_tree.remove_element(-4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_positive_one_right_child_height(self):#double rotation
    self.__test_tree.insert_element(-9)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(-2)
    self.__test_tree.remove_element(4)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_positive_two_zero_right_child_height(self):
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(5)
    self.__test_tree.remove_element(0)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_balance_negative_two_zero_right_child_height(self):
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(1)
    self.__test_tree.remove_element(3)#needs balance
    self.assertEqual(3, self.__test_tree.get_height())

  def test_remove_multiple_balance_height(self):
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(-16)
    self.__test_tree.insert_element(16)
    self.__test_tree.insert_element(-24)
    self.__test_tree.insert_element(-8)
    self.__test_tree.insert_element(8)
    self.__test_tree.insert_element(24)
    self.__test_tree.insert_element(-28)
    self.__test_tree.insert_element(-20)
    self.__test_tree.insert_element(-4)
    self.__test_tree.insert_element(4)
    self.__test_tree.insert_element(12)
    self.__test_tree.insert_element(20)
    self.__test_tree.insert_element(28)
    self.__test_tree.insert_element(-30)
    self.__test_tree.insert_element(6)
    self.__test_tree.insert_element(10)
    self.__test_tree.insert_element(14)
    self.__test_tree.insert_element(30)
    self.__test_tree.insert_element(15)
    self.__test_tree.remove_element(20)
    self.assertEqual(5, self.__test_tree.get_height())

  def test_to_list_empty(self):#tests to_list traversal of an empty tree
    self.assertEqual([], self.__test_tree.to_list())

  def test_to_list_height_one(self):#tests to_list traversal of a tree of height 1
    self.__test_tree.insert_element(1)
    self.assertEqual([1], self.__test_tree.to_list())

  def test_to_list_height_two(self):#tests to_list traversal of a tree of height 2
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.assertEqual([0,1,2], self.__test_tree.to_list())

  def test_to_list_height_three(self):#tests to_list traversal of a tree of height 3
    self.__test_tree.insert_element(1)
    self.__test_tree.insert_element(-1)
    self.__test_tree.insert_element(3)
    self.__test_tree.insert_element(-2)
    self.__test_tree.insert_element(0)
    self.__test_tree.insert_element(2)
    self.__test_tree.insert_element(4)
    self.assertEqual([-2,-1,0,1,2,3,4], self.__test_tree.to_list())

if __name__ == '__main__':
  unittest.main()
