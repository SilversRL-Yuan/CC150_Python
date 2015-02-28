#2.1Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?
import linkedlist
l1 = linkedlist.LinkedList()
print(l1)
l1.AddNode(3)
l1.AddNode(7)
l1.AddNode(3)
l1.AddNode(5)
print(l1)
l1.InsertNode(3, 2)
def remove_dup(lists):
	nodelists = []
	node = lists.head
	while node:
		if node.data not in nodelists:
			nodelists.append(node.data)
			prev_node = node
		else:
			prev_node.next = node.next
		node = node.next
	return nodelists
#print(remove_dup(l1))

def remove_dup_nobuff(lists):
	node = lists.head
	while node:
		current = node
		prev = current
		while current:
			if current.data != node.data:
				prev = current
			else:
				prev.next = current.next
			current = current.next
		node = node.next
	return lists

print(remove_dup_nobuff(l1))

