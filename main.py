"""
Usage:
    dojo create_room <room_type> <room_names>...
    dojo add_person <person-attributes>...
    dojo (-i | --interactive)
    dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo
dojo = Dojo()
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
class RoomAllocationSystem (cmd.Cmd):
    intro = 'WELCOME THE ROOM ALLOCATION SYSTEM (TRAS)' \
     + ' (Enter help for a list of commands.)'
    prompt = 'TRAS/> '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_names>... """
        room_type = args['<room_type>']
        room_names = args['<room_names>']
        for room_name in room_names:
        	print(dojo.create_room(room_type, room_name))
            
    @docopt_cmd
    def do_add_person(self, args): 
        """Usage: add_person <person_attributes>... """
        #Calling add person with different arguments for different cases
        person_attributes = args['<person_attributes>']
        if len(person_attributes) == 2:
            print(dojo.add_person(person_attributes[0], person_attributes[1], "N"))
        elif len(person_attributes) == 3 and (person_attributes[2] == 'N' or person_attributes[2] == 'Y'):
            print(dojo.add_person(person_attributes[0], person_attributes[1], person_attributes[2]))
        elif len(person_attributes) == 3 and person_attributes[2] != 'N' or person_attributes[2] != 'Y':
            person_name = person_attributes[0] + " " + person_attributes[1]
            print(person_name)
            print(dojo.add_person(person_name, person_attributes[2], 'N'))
        elif len(person_attributes) == 4 and (person_attributes[3] == 'N' or person_attributes[3] == 'Y'):
            person_name = person_attributes[0] + " " + person_attributes[1]
            print(dojo.add_person(person_name, person_attributes[2], person_attributes[3]))
        else:
            print("Please Enter: add_person <first_name> <last_name> <fellow/staff> <wants_accomodation:N/Y>")
    
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    RoomAllocationSystem().cmdloop()
print(opt)