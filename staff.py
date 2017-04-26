from person import Person

class Staff(Person):

	def __init__(self, name, person_type, office):
	 	Person.__init__(self, name, person_type, office)