#!/usr/bin/env python
## Complete Example of Class and Generators usage 
import pdb

class Node(object):
    node_data = None
    next_node_ptr = None
    def __init__(self, data):
        self.node_data = data

    def addNode(self, new_node):
        self.next_node_ptr = new_node

    def printNodes(self):
        final_node = self
        while final_node :
            yield final_node.node_data ;
            final_node = final_node.next_node_ptr

    def addNodes(self, obj_array):
        for  item in obj_array :
            tip_of_list = self
            while tip_of_list.next_node_ptr :
                last_data = self.node_data
                tip_of_list = tip_of_list.next_node_ptr
            tip_of_list.next_node_ptr = Node(item)

    def reverseList(self) :
        initial_node = self
        final_node = None
        while initial_node  :
            initial_node.next_node_ptr , initial_node , final_node = final_node, initial_node.next_node_ptr , initial_node
        return final_node



another = Node(-11)
another.addNodes(range(12))


# Generator Example
for item in another.printNodes():
    print item , "",
print

# Generator Example

for item in another.reverseList().printNodes():
    print item , "",
print
