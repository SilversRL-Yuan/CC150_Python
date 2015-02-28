class Node:
	"""docstring for Node."""
	def __init__(self, data = None, next = None):
		self.data = data	
		self.next = next

class LinkedList:
	"""This LinkedList has AddNode, DelNode, InsertNode in_place Qsort and GetLeng methods."""
	def __init__(self):
		#self.current_node = Node()
		self.head = Node()
		self.current_node = Node()
		#self.tail = Node()

	def __str__(self):
		"""Return a str(list) that contains data in order."""
		data_list = []
		indexing_node = self.head
		while indexing_node:
			data_list.append(indexing_node.data)
			indexing_node = indexing_node.next

		return str(data_list)

	def AddNode(self, data):
		new_node = Node(data, None)	

		if self.head.data:  # if not empty
			self.current_node.next = new_node# make old tail node point to new node
			self.current_node = self.current_node.next
		else:
			self.head = new_node
			self.current_node = self.head

	def DelNode(self, data):
		'''Delete the node with data.'''
		indexing_node = self.head
		while indexing_node.next:
			if indexing_node.next.data == data:
				indexing_node.next = indexing_node.next.next
				break
			indexing_node = indexing_node.next
		else:
			print('No data found!')
			raise ValueError(data)

	def InsertNode(self, data, data_new): 
		'''Insert one node after the node with data.'''
		indexing_node = self.head
		while indexing_node.next:  # if not last one
			if indexing_node.data == data:
				new_node = Node(data_new, None)
				new_node.next = indexing_node.next
				indexing_node.next = new_node
				break
			indexing_node = indexing_node.next
		else:
			print('No data found!')
			raise ValueError(data)

	def GetLeng(self):
		indexing_node = self.head
		i = 1
		while indexing_node.next:
			i += 1
			indexing_node = indexing_node.next
		return i

	def Reverse(self):
		'''Reverse the Single LinkedList'''
		node = self.head
		node_list = [node]
		while node.next:
			node_list.append(node.next)
			node = node.next

		self.head = node
		while len(node_list) > 0:
			node.next = node_list.pop()
			node = node.next
		node.next = None


# test
#ll = LinkedList()
#ll.AddNode(3)
#ll.AddNode(7)
#ll.AddNode(5)
#ll.InsertNode(3, 2)
