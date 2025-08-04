from Linked_List import LinkedList

list=LinkedList()

list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")
list.print_list()
print("Length:", list.getlength())


#swapping nodes
def swapping(list,key1,key2):
    if key1==key2:
       return "key is same"

    prev1=None
    prev2=None
    curr1=list.head
    curr2=list.head

    while curr1 is not None and key1!=curr1.data:
        prev1=curr1
        curr1=curr1.next
    while curr2 is not None and key2 != curr2.data:
        prev2 = curr2
        curr2 = curr2.next

    if not curr1 or not curr2:
        return "not possible"

    if prev1:
        prev1.next = curr2
    else:
        list.head = curr2

    if prev2:
        prev2.next = curr1
    else:
        list.head = curr1

    curr1.next, curr2.next = curr2.next, curr1.next




def len_recursive(self, node):
  if node is None:
    return 0
  return 1 + self.len_recursive(node.next)


def swapping(list, key_1, key_2):
    if key_1==key_2:
        return "same key"

    prev1=None
    curr1=list.head

    while curr1 is not None and key_1!=curr1.data:
        prev1=curr1
        curr1=curr1.next

    prev2 = None
    curr2 = list.head

    while curr2 is not None and key_2 != curr2.data:
        prev2 = curr2
        curr2 = curr2.next

    if curr1 is None or curr2 is None:
        return "KEY NOT FOUND"

    if prev1:
        prev1.next=curr2
    else:
        list.head=curr2
    if prev2:
        prev2.next = curr1
    else:
         list.head = curr1

    curr1.next, curr2.next = curr2.next, curr1.next

def reverse(head):
    if head is None or head.next is None:
        return head

    newHead = reverse(head.next)
    head.next.next = head
    head.next = None
    return newHead

# Swapping example
swapping(list, 'B', 'C')
list.print_list()

print("Reversed:")
list.head = reverse(list.head)
list.print_list()


