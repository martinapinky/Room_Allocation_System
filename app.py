#!/usr?bin?env python
"""
Usage:
	dojo create_room <room_type> <room_names>...
	dojo (-i | ---interactive)
	dojo (-h | --help | --version)
Options:
	-i, --interactive Interactive Mode
	-h, --help Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo 

dojo = Dojo()
def docopt_cmd(func):
	"""
	This decorator is used to simplify the try/except block and pass the result of the 
	docopt parsing to the called action.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			# The DocoptExit is thrown when the args do not match.
			# We print a message to the user and the usage block.
			print('Please Enter Correct Command')
			print(e)
			return
		except SystemExit:
			# The SystemExit exception prints the usage for --help
			# We do not need to do the print here.
			return
		return func(self, opt)
	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn
class MyInteractive (cmd.Cmd):
	intro = 'Welcome to the Room Allocation System' \
		+ ' (Enter help for a list of commands.)'
	prompt = 'dojo>>> '
	file = None
	@docopt_cmd
	def do_create_room(self, arg):
		"""Usage: create_room [<room_type>] <room_names>... """
		room_type = arg['<room_type>']
		room_names = arg['<room_names>']
		dojo.create_room(room_type, room_names)
		for room in room_name:
			print(room_type + " room " + str(i) + " successfully created\n")

	def do_quit(self, arg):
		"""Quits out of Interactive Mode."""
		print('Goodbye!')
		exit()
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
	MyInteractive().cmdloop()
print(opt)
