#2.2 Find the nth from the end of a singly linkedlist.
#eg. 8->10->5->7->2->1->5->4->10->10 then the result is  7th to last node is 7
import linkedlist
l1 = linkedlist.LinkedList()
print(l1)
l1.AddNode(3)
l1.AddNode(7)
l1.AddNode(3)
l1.AddNode(5)
print(l1)
l1.InsertNode(3, 2)
print(l1)
def Fnd_end_nth(lists,n):
	if n < 1:
		raise ValueError ('pleas input a valid number')
	node = lists.head
	i = 0
	while node is not None:
		node = node.next
		i += 1
	length = i

	if n > length:
		raise ValueError ('n is larger than length of linkedlist')
	m = length - n + 1
	node = lists.head
	i = 1
	while i < m:
		node = node.next
		i += 1
	return node.data
print(Fnd_end_nth(l1,4))
