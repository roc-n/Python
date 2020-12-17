import argparse


def limit(string):
    num = int(string)
    if num < 1:
        return 1
    if num > 10:
        return 10
    return num


parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name')
print(parser.parse_args(['--name', 'Eric']))
print(parser.parse_args([]))


# parser.add_argument('--file', type=open)
# print(parser.parse_args(['--file', 'start.py']))


parser.add_argument('--num', type=limit)
print(parser.parse_args(['--num', '19']))


parser.add_argument('--attribute', default=True, type=bool)
print(parser.parse_args())


parser.add_argument('--mode', choices=('read-only', 'read-write'))
print(parser.parse_args(['--mode', 'read-only']))
