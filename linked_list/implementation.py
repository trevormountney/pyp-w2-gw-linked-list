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
            #else:
            #    raise IndexError

    def __add__(self, other):
        new_linked_list = LinkedList()
        for each in self:
            new_linked_list.append(each)
        for each in other:
            new_linked_list.append(each)
        return new_linked_list

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        self_list = [each for each in enumerate(self)]
        other_list = [each for each in enumerate(other)]
        if self_list == other_list:
            return True
            

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

        '''try:
            while self.next_node != self.end:
                yield self.next_node
                self.next_node = self.next_node.next
        except (AttributeError):
            raise StopIteration'''
            
    

something = LinkedList([5, 6, 7])

'''print(something.start)
print(something.start.next)
print(something.end)
print(something.end.next)'''

for each in something:
    print(each)
    
for each in something:
    print(each)
    
print(len(something))
print(len(something))
print(something.count())
print(something)

print(enumerate(iter(something)) == enumerate(something))
print(something[1])

something2 = LinkedList([5, 6, 9])

print(something + something2)

my_list = LinkedList()
new_list = my_list + LinkedList([1])
#print(new_list == my_list)

print(LinkedList([1] == LinkedList([1])))

print(something2)
print(something2.pop(0))
print(something2)

l1 = LinkedList([9])

print(l1.pop())
print(l1.start)
print(l1.end)
