from office import Office
from livingspace import LivingSpace
from fellow import Fellow
from staff import Staff
import random

class Dojo(object):
	
	def __init__(self):
		
		self.livingspaces_created = []
		self.offices_created = []
		self.fellows_added = []
		self.staff_added = []

	def create_room(self, room_type, room_name):
		if room_type is None or room_name is None:
			return "Must set room_name and room_type"
		else:
			if self.check_room_exists(room_name) is False:
				if room_type == 'office':
					new_office = Office(room_type, room_name)
					self.offices_created.append(new_office)
					return "An office called " + room_name + " has been successfully created!"
				if room_type == 'livingspace':
					new_livingspace = LivingSpace(room_type, room_name)
					self.livingspaces_created.append(new_livingspace)
					return "A livingspace called " + room_name + " has been successfully created!" 	
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

	def add_person(self, person_name, person_type, wants_accomodation='N'):
		random_office = None
		random_livingspace = None
		if self.get_available_rooms("office"):
			random_office = random.choice(self.get_available_rooms("office"))
		if self.get_available_rooms("livingspace"):
			random_livingspace = random.choice(self.get_available_rooms("livingspace"))

		if person_type == 'fellow':
			if wants_accomodation and wants_accomodation == 'Y':
				new_fellow = Fellow(person_name, "fellow", random_office, random_livingspace)
				self.fellows_added.append(new_fellow)
				if random_office:
					new_fellow.office.number_of_occupants += 1
					print((new_fellow.office.name, str(new_fellow.office.number_of_occupants)))

				if random_livingspace:
					new_fellow.livingspace.number_of_occupants += 1
				return 'Fellow ' + person_name + ' has successfully been added.'
			
			else:
				new_fellow = Fellow(person_name, "fellow", random_office, None)
				self.fellows_added.append(new_fellow)
				if random_office:
					new_fellow.office.number_of_occupants += 1
					print((new_fellow.office.name, str(new_fellow.office.number_of_occupants)))

				return 'Fellow ' + person_name + ' has successfully been added.'

		if person_type == 'staff':
			if wants_accomodation and wants_accomodation == 'Y':
				return 'Staff cannot be allocated livingspace'
			else:
				new_staff = Staff(person_name, "staff", random_office) 
				self.staff_added.append(new_staff)
				if random_office:
					new_staff.office.number_of_occupants += 1
					print((new_staff.office.name, str(new_staff.office.number_of_occupants)))

				return 'Staff ' + person_name + ' has successfully been added.'


	def get_available_rooms(self, room_type):
		available_rooms = []

		if room_type == 'livingspace':
			for livingspace in self.livingspaces_created:
				if livingspace.number_of_occupants < livingspace.maximum_number_of_occupants:
					available_rooms.append(livingspace)

		if room_type == 'office':
			for office in self.offices_created:
				if office.number_of_occupants < office.maximum_number_of_occupants:
					available_rooms.append(office)

		return available_rooms
