/**
 * Definition for singly-linked list.  */
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let result: ListNode | null = null;

  if (list1 === null) {
    return list2;
  }

  if (list2 === null) {
    return list1;
  }

  //   Initialize the head and tail pointers
  let head: ListNode | null = null;
  let tail: ListNode | null = null;

  if (list1.val <= list2.val) {
    head = tail = list1;
    list1 = list1.next;
  } else {
    head = tail = list2;
    list2 = list2.next;
  }

  //   Merge the remaining nodes
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      tail.next = list1;
      tail = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      tail = list2;
      list2 = list2.next;
    }
  }
  //   attach what's left
  tail.next = list1 ? list1 : list2;
  return head;
}
