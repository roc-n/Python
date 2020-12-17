import argparse
import os
from git.cmd import Git


def handle_status(git, args):
    """处理status命令"""
    cmd = ['git', 'status']
    output = git.execute(cmd)
    print(output)


def handle_add(git, args):
    """处理add命令"""
    cmd = ['git', 'add'] + args.pathspec
    output = git.execute(cmd)
    print(output)


def handle_commit(git, args):
    """处理-m <msg>命令"""
    cmd = ['git', 'commit', '-m', args.message]
    output = git.execute(cmd)
    print(output)


def handle_push(git, args):
    cmd = ['git', 'push']
    output = git.execute(cmd)
    print(output)


def cli():
    """git 命名程序入口"""
    parser = argparse.ArgumentParser(prog='git')
    subparsers = parser.add_subparsers(
        title='There are common Git commands used in various situations',
        metavar='command')
    # 也许调用了parser_args()后解析程序就失效了
    # print(parser.parse_args())
    # status
    status_parser = subparsers.add_parser(
        'status', help='Show the working tree status')
    status_parser.set_defaults(handle=handle_status)
    # add
    add_parser = subparsers.add_parser(
        'add', help='Add file contents to the index')
    add_parser.add_argument(
        'pathspec', help='Files to add content from', nargs='*')
    add_parser.set_defaults(handle=handle_add)
    # commit
    commit_parser = subparsers.add_parser(
        'commit', help='Record changes to the repository')
    commit_parser.add_argument(
        '--message', '-m', help='Use the given <msg> as the commit message', metavar='msg', required=True)
    commit_parser.set_defaults(handle=handle_commit)
    # push
    push_parser = subparsers.add_parser(
        'push', help='Update remote refs along with associated objects')
    push_parser.set_defaults(handle=handle_push)

    git = Git(os.getcwd())
    args = parser.parse_args()
    if hasattr(args, 'handle'):
        args.handle(git, args)
    else:
        parser.print_help()


if __name__ == '__main__':
    cli()
