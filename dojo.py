from office import Office
from livingspace import LivingSpace
from fellow import Fellow
from staff import Staff
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

	def add_person(self, person_name, person_type, *wants_accomodation):
		
		if person_type == 'fellow' and self.offices_created and self.livingspaces_created:
			if wants_accomodation and wants_accomodation[0] == 'Y':
				new_fellow = Fellow(person_name, "fellow", random.choice(self.offices_created), random.choice(self.livingspaces_created))
				self.fellows_added.append(new_fellow)
			else:
				new_fellow = Fellow(person_name, "fellow", random.choice(self.offices_created))
				self.fellows_added.append(new_fellow)
		if person_type == 'staff' and self.offices_created and self.livingspaces_created:
			if wants_accomodation and wants_accomodation[0] == 'Y':
				return 'Staff cannot be allocated livingspace'
			else:
				new_staff = Staff(person_name, "staff", random.choice(self.offices_created))
				self.staff_added.append(new_staff)



dojo = Dojo()
# print(dojo.check_room_exists("Fox"))
# dojo.create_room("office", "Office1")
# dojo.create_room("office", "Office2")
# dojo.create_room("office", "Office3")
# dojo.create_room("office", "Office4")
# dojo.create_room("office", "Office5")
# dojo.create_room("livingspace", "livingspace1")
# dojo.create_room("livingspace", "livingspace2")
# dojo.create_room("livingspace", "livingspace3")
# dojo.create_room("livingspace", "livingspace4")
# dojo.create_room("livingspace", "livingspace5")
# print(dojo.offices_created)

room_list = dojo.livingspaces_created + dojo.offices_created
room_names = []
for room in room_list:
	room_names.append(room.name)
print(room_names)
dojo.add_person("Martina", "fellow")
dojo.add_person("Simon", "fellow")
dojo.add_person("Maria", "staff")
dojo.add_person("Humaira", "staff", "Y")

for person in dojo.fellows_added:
	if person.livingspace:
		print((person.name, person.person_type, person.office.name, person.livingspace.name))
	else:
		print((person.name, person.person_type, person.office.name))

for person in dojo.staff_added:
		print((person.name, person.person_type, person.office.name))