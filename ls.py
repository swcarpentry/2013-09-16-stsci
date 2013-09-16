import os
import sys

hidden = False

if len(sys.argv) == 1:
    path = '.'
elif len(sys.argv) == 2:
    if sys.argv[1] == '-a':
        path = '.'
        hidden = True
    else:
        path = sys.argv[1]
elif len(sys.argv) == 3:
    if sys.argv[1] == '-a':
        hidden = True
    path = sys.argv[2]

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
