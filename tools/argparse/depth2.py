import argparse
# add_help设为True自动生成帮助
parser = argparse.ArgumentParser(add_help=True)
# parser.add_argument('--foo')
# print(parser.parse_args(['-h']))
# print("*****************************")


# 自定义帮助，借助formatter_class=argparse.RawTextHelpFormatter实现
parser = argparse.ArgumentParser(add_help=True,
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 description="""
# description
#     raw
#         formatted""")
# parser.add_argument('-a', action="store_true", help="""argument
#     raw
#         formatted""")
# print(parser.parse_args(['-h']))


# 参数组
# parser_1 = argparse.ArgumentParser()
# group = parser_1.add_argument_group('authentication')
# group.add_argument('--user', action="store")
# group.add_argument('--password', action="store")
# parser_1.add_argument('--push', action="store")
# print(parser_1.parse_args(['-h']))

# 选项参数前缀

parser = argparse.ArgumentParser(
    description="Option prefix", prefix_chars='-+/')
parser.add_argument('-power', action="store_false",
                    default=None, help='Set power off')
parser.add_argument('+power', action="store_true",
                    default=None, help='Set power on')
parser.add_argument('/win', action="store_true", default=False)

print(parser.parse_args(['-power']))
print(parser.parse_args(['/win']))
print(parser.parse_args(['+power', '/win']))
