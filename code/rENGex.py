import translator
import sys
from store import help_message, wrong_num_arguments_message

# Base file for running rENGex from the command line.
if len(sys.argv) == 1:
    print(wrong_num_arguments_message)
    exit(0)

if len(sys.argv) > 2:
    print(wrong_num_arguments_message)
    print(f"One argument expected, received {len(sys.argv) - 1}")
    exit(0)

input = sys.argv[1]
args = input.split(" ")

if "-h" in args:    print(help_message)
else:               print(f"Your REGEX is: {translator.parse(args, )} \n")
exit(0)