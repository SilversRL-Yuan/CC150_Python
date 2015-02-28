#2.3 Implement an algorithm to delete a node in the middle of a single 
#linked list, given only access to that node.
#EXAMPLE:
#Input: the node 'c' from a->b->c->d->e
#Result: nothing is returned, but the new linked list is a->b->d->e
import linkedlist
l = linkedlist.LinkedList()
print(l)
def del_mid(mid_node):
	if mid_node is None or mid_node.next is None:
		raise Exception (LinkedList)
	mid_node.data = mid_node.next.data
	mid_node.next = mid_node.next.next
	return lists
