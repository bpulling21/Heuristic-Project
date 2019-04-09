# tour.py
# Author: Brooke Pulling
# Date: April 5 2019
#
# Description: A program which draws out two heuristics connecting 1000 cities 

from edited_linked_list import *
import math
import turtle

class Point:

	''' A class for representing and drawing points in the plane.'''

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def distance_to(self, other):
		'''returns the distance from self to other'''
		distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**(1/2)
		return distance
		
	
	def draw(self, t):
		'''draws a point using a turtle object t'''
		t.penup()
		t.setx(self.x) # the turtle will teleport to the starting point
		t.sety(self.y)
		t.pendown()
		t.dot(3)
		
		
	def draw_to(self,other,t):
		'''draws a line segment from self to other'''
		t.penup()
		t.setx(self.x)
		t.sety(self.y)
		t.pendown()
		t.goto(other.x, other.y) # This isn't a teleport, and will take turtle to the point. 
	
	def __str__(self):
		'''returns a string representation of self in the (x,y) format'''
		return '(' + str(self.x) + ',' + str(self.y) + ')'
	

class Tour:

	''' A class for representing and drawing TSP tours constructed with the nearest-neighbor heuristic. '''
    
	def __init__(self):
		self.__data = Linked_list() 
		self.__size = 0
		self.__length = 0
		
	def draw(self, t):
		node = self.__data.head
		for i in range(self.__size - 1):
			node.item.draw(t)
			node.item.draw_to(node.link.item, t)
			node = node.link
		node.item.draw_to(self.__data.head.item, t)
	
	def get_length(self):
		'''returns the length'''
		return self.__length
	
	def set_length(self, new_length):
		'''sets the length to new length'''
		self.__length = new_length
		
	def get_size(self):
		'''returns the size'''
		return self.__size
	
	def set_size(self, new_size):
		'''sets the size to new size'''
		self.__size = new_size
		
	def get_data(self):
		'''returns the data'''
		return self.__data
	
	def set_data(self, new_data):
		'''sets the size to new size'''
		self.__data = new_data
		
	
	def insert_nearest(self, pt):
		if self.__size <= 1:
			self.__data.append(pt)
			if self.__size == 1:
				self.__length = 2 * pt.distance_to(self.__data.head.item)
				print(self.__length)
			self.__size += 1
		
		else:
			closest_point = self.__data.head
			current_node = self.__data.head
			closest_point_index = 0
			current_min_distance = pt.distance_to(current_node.item)
			for i in range(self.__size - 1):
				# move to the next node
				current_node = current_node.link
				# find the distance between other and self
				current_distance = pt.distance_to(current_node.item)
				# comparing the distance between the two points to see which is shorter 
				if current_distance < current_min_distance:
					# reassigning the closest point title to a different node if current distance is shorter 
					closest_point = current_node
					current_min_distance = current_distance
					closest_point_index = i + 2 #this is i + 2 because a is 0, b is 1, and we want to insert after b (so 2)
			if closest_point_index == self.__size:
			#increment the size ond length of the trip
				dist_from_next = pt.distance_to(self.__data.head.item)
				dist_from_previous_to_next = closest_point.item.distance_to(self.__data.head.item)
				self.__length = self.__length + current_min_distance + dist_from_next - dist_from_previous_to_next
	
			else:
				dist_from_next = pt.distance_to(closest_point.link.item)
				dist_from_previous_to_next = closest_point.item.distance_to(closest_point.link.item)
				self.__length = self.__length + current_min_distance + dist_from_next - dist_from_previous_to_next
			self.__size += 1
			# insert pt after the closest_point
			self.__data.insert(closest_point_index,pt) # we want to insert pt, which is the closest point
	
			
		
	def insert_smallest(self, pt):
		'''processes the Point object pt by inserting it into the current tour (stored in self.data) after a point for which a smallest detour is made.'''
		if self.__size <= 1:
			self.__data.append(pt)
			if self.__size == 1:
				self.__length = 2 * pt.distance_to(self.__data.head.item)
				print(self.__length)
			self.__size += 1
			
		else:
			current_point = self.__data.head
			current_point2 = self.__data.head.link
			# the "distance to" lines of code serve as a basis for comparison with the detours calculated in the for loop
			dist_between_1_and_2 = current_point.item.distance_to(current_point2.item)
			#pt = the new node that is being put into the sequence
			dist_between_current_and_pt = current_point.item.distance_to(pt)
			dist_between_current2_and_pt = current_point2.item.distance_to(pt)
			#the detour is (dist_between_current2_and_pt + dist_between_current_and_pt) - dist_between_1_and_2
			current_min_detour = (dist_between_current2_and_pt + dist_between_current_and_pt) - dist_between_1_and_2
			current_closest_point = current_point #this will be changed in the for loop as other detours get smaller, and current_point changes
			closest_point_tracker = 0
			for i in range(self.__size - 2): # we want to calculate the detour with pt and each current point, so we need to increment current point
				current_point2 = current_point2.link
				current_point = current_point.link # this finds the next node in the list
				# I reassigned these variables in the for loop because the computer doesn't use the incremented values in the for loop to calculate distances on lines 92,94,95
				dist_between_1_and_2 = current_point.item.distance_to(current_point2.item)
				dist_between_current_and_pt = current_point.item.distance_to(pt)
				dist_between_current2_and_pt = current_point2.item.distance_to(pt)
				detour = (dist_between_current2_and_pt + dist_between_current_and_pt) - dist_between_1_and_2
				# instead of appending all the detour values to a list and finding the biggest one there, I compared the detour with the
				#compare val in the for loop (see above) and then changed the compare val to the detour if the detour is smaller than the compare val
				if detour < current_min_detour:
					current_closest_point = current_point
					current_min_detour = detour
					closest_point_tracker = i + 2 #this is i + 2 because a is 0, b is 1, and we want to insert after b (so 2)
			
			# this is checking that the detour is less than just adding the new point at the end of the list
			tail = current_point2.item
			distance_from_tail = pt.distance_to(tail)
			if distance_from_tail < current_min_detour: # if we are adding a point pt to the end, we need to calculate a new journey because the return isn't included in the heuristic
				dist_to_head = pt.distance_to(self.__data.head.item)
				dist_from_tail_to_head = tail.distance_to(self.__data.head.item)
				self.__length = self.__length - dist_from_tail_to_head + dist_to_head + distance_from_tail
				self.__data.append(pt)  # adding the new point at the end of the list
			else:
				self.__data.insert(closest_point_tracker, pt) # adding the new point whereever the detour is the smallest
				self.__length += current_min_detour
			
			#increment the size, self.__length is incremented above
			self.__size += 1
				
			
			
					
					
				
			
		
		
		
		
		
		
    
