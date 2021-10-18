# Stacks and Queues

class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	# insert in queue tail
	def enqueue(self, data):
		if self.head is None:
			self.tail = self.head = Node(data, None)
			return

		# add new node at tail
		self.tail.next_node = Node(data, None)
		self.tail = self.tail.next_node
		return 

	# delete from queue from head
	def dequeue(self):
		if self.head is None:
			return None

		# delete from head
		removed = self.head
		self.head = self.head.next_node

		# if it was the last
		if self.head is None:
			self.tail = None
		
		return removed