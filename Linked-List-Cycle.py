# Time:  O(n)
# Space: O(1)

class Solution(object):
    # 执行时间为56ms的案例
    def hasCycle(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast,slow=head,head
        while fast and slow and fast.next:
            fast,slow=fast.next.next,slow.next
            if fast==slow:
                return True
        return False