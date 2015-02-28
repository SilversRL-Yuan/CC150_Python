#2.6 Given a circular linked list, returns node at the beginning of the loop
#EXAMPLE:
#Input: A->B->C->D->E->C
#Output: C
import linkedlist
def fnd_loop_begin(list):
	node = list.head
	visitedl = {}
	while node:
		if node not in visitedl:
			visitedl[node] = 0
		else:
			break
		node = node.next
	return node.data

ll = linkedlist.LinkedList()
ll.AddNode(1)
ll.AddNode(2)
ll.AddNode(3)
t_node = ll.current_node
print(ll.current_node.data)
ll.AddNode(4)
ll.AddNode(5)
ll.current_node.next = t_node
print(ll.current_node.data)

print(fnd_loop_begin(ll))

