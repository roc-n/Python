import argparse
import base
parser = argparse.ArgumentParser(parents=[base.parser])

parser.add_argument('--ros', action='store_true', default=False,
                    help='Using Ros service to orchestrate cloud resoures')

print(parser.parse_args(['-h']))
