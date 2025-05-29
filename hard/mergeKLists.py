from utils.ListNode import ListNode
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  # type: ignore
        """
        Problem: Merge k sorted Lists; leetcode #23
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.



        Example 1:

        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
        Example 2:

        Input: lists = []
        Output: []
        Example 3:

        Input: lists = [[]]
        Output: []


        Constraints:

        k == lists.length
        0 <= k <= 104
        0 <= lists[i].length <= 500
        -104 <= lists[i][j] <= 104
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 104.
        """

        if not lists:
            return None
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        res_head = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            res_head.next = node
            res_head = res_head.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
