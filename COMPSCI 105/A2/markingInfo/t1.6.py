from trees import *
from testing import *
t = RefBinaryTree(5)
t.insert_left(3)
t.insert_right(6)
t.set_value(9)
display_tree(t.get_right_subtree())
