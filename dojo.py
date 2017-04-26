from office import Office
from livingspace import LivingSpace
import random

class Dojo(object):
	
	def __init__(self):
		# self.number_of_rooms = 
		self.livingspaces_created = []
		self.offices_created = []
		self.fellows_added = []
		self.staff_added = []

	def create_room(self, room_type, *room_names):
		if room_type is None or len(room_names) == 0:
			return "Must set room_name and room_type"
		else:
			for room_name in room_names:
				if self.check_room_exists(room_name) is False:
					if room_type == 'office':
						new_office = Office(room_type, room_name)
						self.offices_created.append(new_office)
					if room_type == 'livingspace':
						self.livingspaces_created.append(LivingSpace(room_type, room_name))
				else:
					return room_name + " already exists"
		
	def check_room_exists(self, name):
		room_list = self.livingspaces_created + self.offices_created
		room_names = []
		for room in room_list:
			room_names.append(room.name)

		if not room_names:
			return False
		elif name in room_names:
			return True
		else:
			return False

	def add_person(self, person_name, *person_type):
		if person_type[0] == 'fellow':
			new_fellow = Fellow()
			self.fellows_added.append(new_fellow)
		if person_type[0] == 'staff':
			self.staff_added.append(new_staff)



dojo = Dojo()
# print(dojo.check_room_exists("Fox"))
dojo.create_room("office", "One")
dojo.create_room("office", "Two")
dojo.create_room("office", "Three")
dojo.create_room("office", "Four")
dojo.create_room("office", "Five")
dojo.create_room("livingspace", "Six")
dojo.create_room("livingspace", "Seven")
dojo.create_room("livingspace", "Eight")
dojo.create_room("livingspace", "Nine")
dojo.create_room("livingspace", "Ten")
# print(dojo.offices_created)

room_list = dojo.livingspaces_created + dojo.offices_created
room_names = []
for room in room_list:
	room_names.append(room.name)
print(room_names)
