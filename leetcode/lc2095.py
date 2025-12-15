# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = prev.next.next

        return head



        # front=head
        # back=head
        # count=0

        # while back:
        #     count += 1
        #     back=back.next

        # mid = count//2
        # count = 0

        # if mid == 0:
        #     return None
        # while True:
        #     count += 1
        #     if count==mid:
        #         front.next = front.next.next
        #         break
        #     front = front.next
           
        # return head



