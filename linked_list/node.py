class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next # we are passing a node object for next

    def __str__(self):
        if self.next:
            return "Node({}) > Node({})".format(self.elem, self.next.elem)
        else:
            return "Node({}) > /".format(self.elem)
            
    def __iter__(self):
        return iter([self.elem])

    def __eq__(self, other):
        try:
            return all([self.elem == other.elem, self.next == other.next])
        #return self.elem == other.elem and self.next == other.next
        except(AttributeError):
            return False
            
    # def __ne__(self, other): # is this needed?
    #     return self.elem != other.elem and self.next != other.next

    def __repr__(self):
        return self.__str__()

