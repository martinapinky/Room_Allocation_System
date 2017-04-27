"""
Usage: mahad.py add_numbers <a> <b>
"""



def add_numbers(a, b):
	return a + b

import docopt


if __name__ == '__main__':
	# print('mamamama', __doc__)
	try:
		args = docopt.docopt(__doc__)
		a = args['<a>']
		b = args['<b>']
		print('{a} + {b} = '.format(a=a, b=b), add_numbers(int(a), int(b)))
	except docopt.DocoptExit as e:
		print('Exception', e)