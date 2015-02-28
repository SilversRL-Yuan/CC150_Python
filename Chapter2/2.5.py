#2.5 You have two numbers represented by a linked list, where each node contains a 
#single digit. The digits are stored in reverse order, such that the 1's digit
#is at the head of the list. Write a function that adds the two numbers and 
#returns the sum as a linked list.
#EXAMPLE:
#input: (3->1->5), (6->9->2)
#Output:9->0->8
import linkedlist
def add_steps(node1,node2,carry,newl):
	if node1 is None and node2 is None:
		return
	sum = carry
	if node1:
		sum = sum + node1.data
	if node2:
		sum = sum + node2.data
	if sum > 9:
		sum = sum -10
		carry = 1
	else:
		carry = 0
	newl.AddNode(sum)
	add_steps(node1.next if node1 else None,node2.next if node2 else None,carry,newl)
	return newl

def add_liknedlist(l1,l2,carry=0):
	newl = linkedlist.LinkedList()
	add_steps(l1.head,l2.head,0,newl)
	return newl


ll1 = linkedlist.LinkedList()
ll2 = linkedlist.LinkedList()
ll1.AddNode(3)
ll1.AddNode(1)
ll1.AddNode(5)

ll2.AddNode(6)
ll2.AddNode(9)
ll2.AddNode(2)
#ll2.AddNode(1)

print(add_liknedlist(ll1, ll2))
