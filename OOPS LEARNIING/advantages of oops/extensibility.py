class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def findMid(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head

    mid = findMid(head)
    right_head = mid.next
    mid.next = None

    left = merge_sort(head)
    right = merge_sort(right_head)

    return merge(left, right)

# Helper function to print the list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage:
arr = [4, 2, 1, 3]
head = createLinkedList(arr)
print("Original list:")
printList(head)

sorted_head = merge_sort(head)
print("Sorted list:")
printList(sorted_head)