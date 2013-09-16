import argparse
import os
import sys

hidden = False

parser = argparse.ArgumentParser(
        description="Lists files and directories")
parser.add_argument('path', metavar='PATH',
                    nargs='?', default='.',
                    help='a directory to list the contents of')
parser.add_argument('--all', '-a', action='store_true',
                    help='show all')
options = parser.parse_args()

hidden = options.all
path = options.path

if not os.path.exists(path):
    print 'File/directory ', path, 'does not exist.'
    sys.exit()

filenames = os.listdir(path)

for filename in filenames:
    if not hidden and filename.startswith('.'):
        continue

    # os.listdir only returns base filenames; we need to join it back to the
    # full path before doing operations like isdir()
    if os.path.isdir(os.path.join(path, filename)):
        # os.sep is / on UNIX-like systems, \ on Windows
        filename = filename + os.sep

    print filename
