import unittest

from dojo import Dojo
from office import Office
from livingspace import LivingSpace
from fellow import Fellow
from staff import Staff

#This class contains testcases for the create_room method
class TestCreateRoom(unittest.TestCase):

#This method tests whether a new office is created
	def test_create_office_successfully(self):
		dojo = Dojo()
		number_of_offices = len(dojo.offices_created)
		new_office = dojo.create_room("office", "Fox")
		new_number_of_offices = len(dojo.offices_created)
		self.assertEqual(number_of_offices + 1, new_number_of_offices, msg='New office Not Added')

#This method tests whether a new living space is created
	def test_create_livingspace_successfully(self):
		dojo = Dojo()
		number_of_livingspaces = len(dojo.livingspaces_created)
		new_livingspace = dojo.create_room("livingspace", "Uganda")
		new_number_of_livingspaces = len(dojo.livingspaces_created)
		self.assertEqual(number_of_livingspaces + 1, new_number_of_livingspaces, msg='New livingspace Not Added')

#This method tests whether a TypeError is raised when all/some arguments are not passed, it also tests whether the create_room method returns the right message
	def test_create_room_without_passing_arguments_unsuccessfully(self):
		dojo = Dojo()
		self.assertRaises(TypeError, dojo.create_room)
		self.assertEqual(dojo.create_room("Uganda"), "Must set room_name and room_type", msg='Arguments not set')
		self.assertEqual(dojo.create_room("livingspace"), "Must set room_name and room_type", msg='Arguments not set')

#This method tests whether the create_room method returns the right message when there is an attempt to create a room that already exists
	def test_create_room_already_taken(self):
		dojo = Dojo()
		dojo.create_room("office", "MergeConflict")
		self.assertEqual(dojo.create_room("office", "MergeConflict"), "MergeConflict already exists", msg='Room already exists')
		self.assertEqual(dojo.create_room("livingspace", "MergeConflict"), "MergeConflict already exists", msg='Room already exists')

#This class contains testcases for the add_person method
class TestAddPerson(unittest.TestCase):

#This method tests whether a new fellow is added	
	def test_add_fellow_successfully(self):
		dojo = Dojo()
		dojo.create_room("office", "Office1")
		dojo.create_room("office", "Office2")
		dojo.create_room("livingspace", "livingspace1")
		dojo.create_room("livingspace", "livingspace2")
		number_of_fellows = len(dojo.fellows_added)
		new_fellow = dojo.add_person("Martina", "fellow")
		new_number_of_fellows = len(dojo.fellows_added)
		self.assertEqual(number_of_fellows + 1, new_number_of_fellows, msg='New fellow Not Added')

#This method tests whether a new staff member is added
	def test_add_staff_successfully(self):
		dojo = Dojo()
		dojo.create_room("office", "Office1")
		dojo.create_room("office", "Office2")
		dojo.create_room("livingspace", "livingspace1")
		dojo.create_room("livingspace", "livingspace2")
		number_of_staff = len(dojo.staff_added)
		new_staff = dojo.add_person("Maria", "staff")
		new_number_of_staff = len(dojo.staff_added)
		self.assertEqual(number_of_staff + 1, new_number_of_staff, msg='New staff Not Added')

#This method tests whether a fellow who wants accommodation is added
	def test_add_fellow_with_accommodation_successfully(self):
		dojo = Dojo()
		dojo.create_room("office", "Office1")
		dojo.create_room("office", "Office2")
		dojo.create_room("livingspace", "livingspace1")
		dojo.create_room("livingspace", "livingspace2")
		number_of_fellows = len(dojo.fellows_added)
		new_fellow = dojo.add_person("Martina", "fellow", "Y")
		new_number_of_fellows = len(dojo.fellows_added)
		self.assertEqual(number_of_fellows + 1, new_number_of_fellows, msg='New fellow Not Added')

#This method tests whether a staff member who wants accomodation is not added as staff cannot be allocated livingspace
	def test_add_staff_with_accommodation_unsuccessfully(self):
		dojo = Dojo()
		dojo.create_room("office", "Office1")
		dojo.create_room("office", "Office2")
		dojo.create_room("livingspace", "livingspace1")
		dojo.create_room("livingspace", "livingspace2")
		number_of_staff = len(dojo.staff_added)
		new_staff = dojo.add_person("Maria", "staff", "Y")
		new_number_of_staff = len(dojo.staff_added)
		self.assertEqual(number_of_staff, new_number_of_staff, msg='Staff cannot be allocated livingspace')

#This method tests whether a new fellow is not when there are no rooms created. No rooms = Cannot add Person
	def test_add_fellow_with_no_rooms_unsuccessfully(self):
		dojo = Dojo()
		number_of_fellows = len(dojo.fellows_added)
		new_fellow = dojo.add_person("Martina", "fellow", "Y")
		new_number_of_fellows = len(dojo.fellows_added)
		self.assertEqual(number_of_fellows, new_number_of_fellows, msg='No rooms to allocate. New Fellow Not Supposed to Added')

if __name__ == "__main__":
	unittest.main()