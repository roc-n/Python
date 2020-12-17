import argparse
import base

parser = argparse.ArgumentParser(parents=[base.parser])
parser.add_argument('--cloudinformation', action="store_true", default=False,
                    help="Using Cloudformation service to orchestrate cloud resources")

print(parser.parse_args(['-h']))
