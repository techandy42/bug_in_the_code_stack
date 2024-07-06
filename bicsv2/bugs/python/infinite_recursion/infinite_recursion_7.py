class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    rest = reverse_linked_list(head)
    head.next.next = head
    head.next = None
    return rest
