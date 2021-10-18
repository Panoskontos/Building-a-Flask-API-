class Node:
	def __init__(self,data,next_node):
		self.data = data
		self.next_node = next_node

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None

	def peek(self):
		return self.top

	def push(self, data):
		if self.top is None:
			self.top = self.bottom = Node(data, None)

		prev_top = self.top
		new_top = Node(data, prev_top)
		self.top = new_top


	def pop(self):
		if self.top is None:
			return None

		remove = self.top
		self.top = self.top.next_node
		return remove

