#  we will use this data structure

class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


class LinkedList:
	def  __init__(self):
		self.head = None
		self.last_node = None


	# visual representation of our list
	
	def print_ll(self):
		ll_string = ""
		node = self.head
		if node is None:
			print(None)
		else:
			while node:
				ll_string += f"{str(node.data)} -> "	
				node = node.next_node
			
			ll_string += " None"
			print(ll_string)




	# add methods to insert at the begining
	def insert_begining(self, data):
		# if it is empty
		if self.head is None:
			self.head = Node(data, None)
			self.last_node = self.head

		# if it is not empty
		new_node = Node(data, self.head)
		self.head = new_node




	# add methods to insert at the end
	def insert_at_the_end(self, data):
		# if it is empty
		if self.head is None:
			self.insert_begining(data)
			return
			

		# if it is not,add the last node
		self.last_node.next_node = Node(data, None)
		self.last_node = self.last_node.next_node

# convert our data to list for json
	def to_list(self):
		arr = []
		if self.head is None:
			return arr
		# if list is not empty
		node = self.head
		while node:
			arr.append(node.data)
			node = node.next_node
		return arr

# method to find specific user by id
	def get_user_by_id(self, user_id):
		node = self.head
		while node:
			if node.data["id"] is int(user_id):
				return node.data
			node = node.next_node
		return None


# ll = LinkedList()
"""
node3 = Node("data3", None)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1
ll.insert_begining("data_fixed")
ll.insert_at_the_end("end")
"""
# ll.insert_begining("end")
# ll.print_ll()
