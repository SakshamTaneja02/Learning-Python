#clu are programs that can be run from the terminal or command line interface and they are an essential part of many development workflows
import argparse
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)
