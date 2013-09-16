import os
import sys


def list_files(path, hidden=False):
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
