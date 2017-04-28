from room import Room

class LivingSpace(Room):
	def __init__(self, room_type, name):
		Room.__init__(self, room_type, name)  
		self.maximum_number_of_occupants = 4