#2.7 Implement a function to check if a linked list is a palindrome.
import linkedlist
ll1 = linkedlist.LinkedList()
print(ll1)
ll1.AddNode(1)
ll1.AddNode(2)
ll1.AddNode(3)
ll1.AddNode(2)
ll1.AddNode(1)
#ll1.AddNode(2)
print(ll1)
def check_palindrome(list):
	newl = []
	head = list.head
	while head:
		newl.append(head.data)
		head = head.next
	if newl == newl[::-1]:
		return True
	else:
		return False

print(check_palindrome(ll1)) 
