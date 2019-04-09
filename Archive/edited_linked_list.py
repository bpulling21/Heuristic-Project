# linked_list.py
# Brooke Pulling
# 2019-02-12
# A link-based implementation of the List ADT.

import node

class Linked_list:
	def __init__(self, seq = ()):
		
		'''Creates a Linked_list object.'''

		self.head = None # Head node of the list
		self.length = 0 # The number of items in the list
		
		# this for lopp is creating the linked list "self". 
		for item in seq:
			self.append(item)
			item = prev_node
			prev_node = prev_node.link
			prev_node = prev_node + 1
			

	def __len__(self):

		'''Returns the number of items in the list.'''

		return self.length

	def append(self, item):

		'''Appends an item to the end of the list.'''

		new_node = node.Node(item)

		if self.head is None:
			self.head = new_node
		
		else:
			end_node = self.find(self.length - 1)
			end_node.link = new_node
		self.length = self.length + 1
			
			
	def find(self, position):

		'''Returns the node at the specified position in the list'''

		next_node = self.head

		for i in range(position):
			next_node = next_node.link

		return next_node
	
	def __getitem__(self, position): # position 0 is the first number in the list
		'''this function returns the item at a specified position'''
		current_node = self.head
		for i in range(position):
			current_node = current_node.link
		return current_node
	
	def __setitem__(self, position, item): # position 0 is the first number in the list
		'''this function allows the item at a specified position to be changed to something else'''
		current_node = self.head
		for i in range(position):
			current_node = current_node.link
		current_node.item = item
	
	def insert(self, position, item):
		'''this function inserts a node at a given position'''
		# first make a new node
		new_node = node.Node(item)
		# find the node right before it
		before_node = self.__getitem__(position - 1)
		# save the node that comes after the new node
		after_node = before_node.link
		# set the link of before node to the new node
		before_node.link = new_node
		# set the link of the new node to the after node
		new_node.link = after_node
		# increment length
		self.length = self.length + 1
	
	def clear(self):
			'''this function clears all the items from a list'''
			self.head = None
			self.length = 0
			
	def reverse(self, position, item):
		'''reverses the string'''
		for i in range(self.length):
			self.head.item = self.head(len(my_list) - i) #sets the head item to the head of the reverse position
			#previous_node = self.find(self.length - i)
			
			
	
	def __delitem__(self, position):
		self._delete(position)
	
	def pop(self): 
		position = (self.length - 1)
		return self._delete(position)
	
	
	def _delete(self, position):
		'''private method to delete an item at the specified location, the removed item is returned'''
		
		if position == 0:
			item = self.head.item
			self.head = self.head.link # making the first node return its link
			
		else:
			# find the previous node so that we can connect it to the node after item
			prev_node = self.find(position - 1)
			# save the item by storing it in a value
			item = prev_node.link.item
			# the link of the previous node is now referencing the node after item, skipping over item directly to the next node
			prev_node.link = prev_node.link.link
			
			
			
		self.length = self.length - 1
		return item 
		   
	def __str__(self):
		'''returns a string of the linked_list object: basically this function takes the linked list and prints it so that it looks like a regular list'''
		node = self.head
		if node != None:
			output = '['
			# populate the output string with list items
			for i in range(self.length):
				output = output + str(node.item) + ','
				node = node.link
				
			#output = output + str(node.item)
		
			output = output + ']'
			
			return output
		else:
			return "no list yet"




