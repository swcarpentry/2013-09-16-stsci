import argparse
import ls


def main():
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

    ls.list_files(path, hidden=hidden)


if __name__ == '__main__':
    main()
