import unittest

from dojo import Dojo
from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff


class TestCreateRoom(unittest.TestCase):
	def test_create_office_successfully(self):
		number_of_offices = len(Office.get_all_offices)
		new_office = Dojo.create_room("Fox", "office")
		new_number_of_offices = len(Office.get_all_offices)
		self.assertEqual(number_of_offices + 1, new_number_of_offices, msg='New office Not Added')

	def test_create_livingspace_successfully(self):
		number_of_livingspaces = len(LivingSpace.get_all_livingspaces)
		new_livingspace = Dojo.create_room("Uganda", "livingspace")
		new_number_of_livingspaces = len(LivingSpace.get_all_livingspaces)
		self.assertEqual(number_of_livingspaces + 1, new_number_of_livingspaces, msg='New livingspace Not Added')

	def test_create_room_without_passing_arguments_unsuccessfully(self):
		self.assertEqual(Dojo.create_room(), "Must specify set room_name and room_type", msg='Arguments not set')
		self.assertEqual(Dojo.create_room("Uganda"), "Must specify set room_name and room_type", msg='Arguments not set')
		self.assertEqual(Dojo.create_room("livingspace"), "Must specify set room_name and room_type", msg='Arguments not set')

	def test_create_room_already_taken(self):
		new_office = Dojo.create_room("MergeConflict", "office")
		self.assertEqual(Dojo.create_room("MergeConflict", "office"), "MergeConflict already exists", msg='Room already exists')
		self.assertEqual(Dojo.create_room("MergeConflict", "livingspace"), "MergeConflict already exists", msg='Room already exists')

class TestAddPerson(uniitest.TestCase):
	def test_add_fellow_successfully(self):
		number_of_fellows = len(Fellow.get_all_fellows)
		new_fellow = Dojo.add_person("Martina", "fellow")
		new_number_of_fellows = len(Fellow.get_all_fellows)
		self.assertEqual(number_of_fellows + 1, new_number_of_fellows, msg='New fellow Not Added')

	def test_add_staff_successfully(self):
		number_of_staff = len(Staff.get_all_staff)
		new_staff = Dojo.add_person("Maria", "staff")
		new_number_of_staff = len(Staff.get_all_staff)
		self.assertEqual(new_number_of_staff + 1, new_number_of_staff, msg='New staff Not Added')

	def test_add_fellow_with_accommodation_successfully(self):
		number_of_fellows = len(Fellow.get_all_fellows)
		new_fellow = Dojo.add_person("Martina", "fellow", "Y")
		new_number_of_fellows = len(Fellow.get_all_fellows)
		self.assertEqual(number_of_fellows + 1, new_number_of_fellows, msg='New fellow Not Added')
		self.assertFalse(new_fellow.livingspace is None, msg='New fellow Not allocated livingspace')

	def test_add_staff_with_accommodation_unsuccessfully(self):
		new_staff = Dojo.add_person("Maria", "staff", "Y")
		self.assertEqual(new_staff, "No livingspaces for staff", msg='Staff cannot be allocated livingspace')

