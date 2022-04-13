class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            curr=head
            next1=None
            prev=None
            while curr:
                next1=curr.next
                curr.next=prev
                prev=curr
                curr=next1
            
            return prev
        def compare(head1,head2):
            temp1 = head1
            temp2 = head2
         
            while (temp1 and temp2):
                if (temp1.val == temp2.val):
                    temp1 = temp1.next
                    temp2 = temp2.next
                else:
                    return 0
                 
        # Both are empty return 1
            if (temp1 == None and temp2 == None):
                return 1
            return 0
        slow=head
        fast=head
        prev_slow=head
        midnode=None
        res=True
        if head!=None and head.next!=None:
            while fast!=None and fast.next!=None:
                fast=fast.next.next
                prev_slow=slow
                slow=slow.next
            if fast!=None:
                midnode=slow
                slow=slow.next
            second_half=slow
            prev_slow.next=None
            second_half = reverse(second_half)
            res = compare(head, second_half) 
            second_half = reverse(second_half)
            if midnode!=None:
                prev_slow.next=midnode
                midnode.next=second_half
            else:
                prev_slow=second_half
        return res