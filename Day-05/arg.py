import sys
import argparse

print(sys.argv)

arg_parser = argparse.ArgumentParser("Demo for argparse")

arg_parser.add_argument("input", type=str, help="Input text to print")
arg_parser.add_argument("--count", "-c", type=int, default=1, help="Number of times to print the text")
arg_parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

args = arg_parser.parse_args()

for i in range(args.count):
    if args.verbose:
        print(f"Verbose: Printing text {i + 1} times")
    print(args.input)
