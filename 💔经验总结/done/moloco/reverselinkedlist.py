def reverseList(self, head):
    new_list = None
    current = head

    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node
    
    return new_list