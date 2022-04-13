class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1=headA
        ptr2=headB
        if ptr1==None or ptr2==None:
            return None
        while ptr1!=ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next
            if ptr1==ptr2 :
                return ptr1 
            if ptr1==None:
                ptr1=headB
            if ptr2==None:
                ptr2=headA
        return ptr1