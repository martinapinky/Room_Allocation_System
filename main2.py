"""
Usage: main.py create_room <room_type> <room_name>
"""

from dojo import Dojo 

dojo_instance = Dojo()

import docopt

def create_room(room_type, room_name):

if __name__ == '__main__':
	try:
		args = docopt.docopt(__doc__)
		room_name = args['<room_name>']
		room_type = args['<room_type>']
		print(dojo_instance.create_room(room_type, room_name))

	except docopt.DocoptExit as e:
		print('Exception', e)