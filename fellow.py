from person import Person

class Fellow(Person):

	def __init__(self, name, person_type, office, livingspace):
	 	Person.__init__(self, name, person_type, office)
	 	self.livingspace = livingspace