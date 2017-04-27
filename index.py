""" This example uses docopt with the built in cmd module

Usage:

    (dojo)
    (dojo) create_room <room_type> <room_name>
    (dojo) (-h | --help)

Options:
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo

dojo_instance = Dojo()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class RoomManagement(cmd.Cmd):
    intro = 'Welcome to the Room Management System type help for a list of commands.'
    prompt = '(dojo)'
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""
        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        print(arg)
        # message = dojo_instance.create_room(room_type, room_name)
        # print(message)
        # print('gegfuifhe')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])
RoomManagement().cmdloop()     

