import translator
import sys

if len(sys.argv) > 2:
    print(f"One argument expected, received {len(sys.argv) - 1}")
    print("Please pass all arguments inside of single quotes to avoid shell expansion")
    exit(0)

input = sys.argv[1]
args = input.split(" ")

if args == "-h": print("Help message here")
print(f"Your REGEX is: {translator.parse(args, )}")
