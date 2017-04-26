from room import Room

class Office(Room):
	def __init__(self, room_type, name):
		Room.__init__(self, room_type, name)  #inherits from class Room
	 	
