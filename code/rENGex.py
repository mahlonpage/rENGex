import translator
import sys
from store import help_message

# Base file for running rENGex from the command line.
if len(sys.argv) > 2:
    print(f"One argument expected, received {len(sys.argv) - 1}")
    print("Please pass all arguments inside of single quotes to avoid shell expansion")
    exit(0)

input = sys.argv[1]
args = input.split(" ")

if "-h" in args:    print(help_message)
else:               print(f"Your REGEX is: {translator.parse(args, )}")
exit(0)