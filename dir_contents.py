#! /usr/bin/python3

import os, os.path, sys

# check for presence of ONE command line arg
if len(sys.argv) != 2:
	print('call with directory path')
	sys.exit(-1)		# return "false"

dir = sys.argv[1]

print('contents of {}\n'.format(dir))
for item in os.listdir(dir):
	if item[0] == '.':	# don't show hidden files
		continue
	if os.path.isdir(os.path.join(dir, item)):
		print('dir:  ', end='')
	else:
		print('file: ', end='')
	print(os.path.basename(item))

sys.exit(0)				# return "true"
