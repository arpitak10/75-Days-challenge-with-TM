class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev=None
            next1=None
            curr=node
            while curr!=None:
                next1=curr.next
                curr.next=prev
                prev=curr
                curr=next1
            return prev
        l1=reverse(l1)
        l2=reverse(l2)
        head=l1
        print(head)
        #print(l1)
        #print(l2)
        sum1=0
        carry=0
        prev=None
        while l1!=None and l2!=None:
            print(l1.val,l2.val)
            s=(l1.val+l2.val+carry)
            sum1=s%10
            carry=s//10
            l1.val=sum1
            print(l1.val,sum1)
            prev=l1
            l1=l1.next
            l2=l2.next 
        if l1!=None or l2!=None:
            if l2!=None:
                prev.next=l2
            l1=prev.next
            while l1!=None:
                s=carry+l1.val
                sum1=s%10
                carry=s//10
                l1.val=sum1
                prev=l1
                l1=l1.next
        if carry>0:
            prev.next=ListNode(carry)
        head=reverse(head)
        return head