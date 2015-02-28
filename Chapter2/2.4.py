#2.4Write code to partition a linked list around a value x, such that all nodes less than
#x come before all nodes greater than or equal to x.
import linkedlist
def partition_list(list,x):
	head = list.head
	smaller,larger = linkedlist.LinkedList(),linkedlist.LinkedList()
	smaller1,larger1 = smaller,larger
	# important to copy the first 0 for further link small to larger 0
	while head != None:
		if head.data < x:
			smaller.next = head
			smaller = smaller.next
		else:
			larger.next = head
			larger = larger.next
		head = head.next
	#linke smaller last to the first of larger
	smaller.next = larger1.next
	larger.next = None
	return smaller.next

ll1 = linkedlist.LinkedList()
ll1.AddNode(3)
ll1.AddNode(1)
ll1.AddNode(5)
ll1.AddNode(4)
ll1.AddNode(9)
ll1.AddNode(2)
print(ll1)
s = partition_list(ll1,4)
print(s)




