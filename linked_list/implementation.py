#from .interface import AbstractLinkedList
#from .node import Node
from interface import AbstractLinkedList
from node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            for elem in elements:
                self.append(elem)
        self.next_node = self.start

    def __str__(self):
        return str([each.elem for each in self])

    def __len__(self):
        return sum((1 for each in self))

    def __iter__(self):
        '''code if not using next (not tested in all situations) - now obsolete
        
        next_node = self.start.next
        node_list = [self.start] # are lists allowed in this project?
        if next_node:
            while next_node != self.end:
                node_list.append(next_node)
                next_node = next_node.next
            else:
                node_list.append(self.end)
        return iter(node_list)
        '''
        '''if self.start == self.end:
            return iter(self.start)
        else:'''
        self.next_node = self.start
        return self
        
        
    def __getitem__(self, index):
        for i, v in enumerate(self):
            if i == index:
                return v.elem
            
        raise IndexError

    def __add__(self, other):
        new_linked_list = LinkedList()
        for each in self:
            new_linked_list.append(each.elem)
        for each in other:
            new_linked_list.append(each.elem)
        return new_linked_list

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        self_list = [each for each in enumerate(self)]
        other_list = [each for each in enumerate(other)]
        return self_list == other_list
            
    def __ne__(self, other):
        self_list = [each for each in enumerate(self)]
        other_list = [each for each in enumerate(other)]
        return not self_list == other_list

    def append(self, elem):
        node = Node(elem)
        
        if self.start is None:
            self.start = node
          
        elif self.end is None:
            self.start.next = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def count(self):
        return len(self)

    def pop(self, index=None):
        
        # Raise error if empty list
        if self.start is None:
            raise IndexError
        
        if index > len(self) - 1:
            print(len(self))
            raise IndexError
        
        if self.start.next is None:
            return_elem = self.start.elem
            self.start = None
            return return_elem
        
        if index == 0:
            return_elem = self.start.elem
            self.start = self.start.next
            return return_elem
        
        if index is None:
            index = len(self) - 1
        
        
        count = 0
        previous = None
        current = self.start
        
        while index != count:
            previous = current
            current = current.next
            count += 1
        else:
            previous.next = current.next
            return current.elem
            
        #return self[index]

    
    
    def next(self):
        try: 
            if self.next_node is None:
                raise StopIteration
            else:
                result = self.next_node
                self.next_node = self.next_node.next
                return result
        except(AttributeError):
            raise StopIteration

