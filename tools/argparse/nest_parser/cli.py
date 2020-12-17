import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help="commands")
# Create
create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument(
    'dirname', action='store', help='New directory to create')

# Delete
delete_parser = subparsers.add_parser('delete', help='Remove a directory')
delete_parser.add_argument('dirname', action='store',
                           help='The directory to remove')
delete_parser.add_argument('--recursive', '-r', default=False,
                           action='store_true', help='recursively remove the directory')
print(parser.parse_args())
