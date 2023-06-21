import translator
import sys
from store import flags, character_classes

def parse(args):
    regex = ""
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in flags:
            extra_args = flags[arg]
            if   arg == "-nocase":      regex =  "(?i)" + regex
            elif arg == "-lit":         regex += translator.lit(args[i+1])
            elif arg == "-in":          regex += translator.rengex_in(args[i+1])
            elif arg == "-notin":       regex += translator.notin(args[i+1])
            elif arg == "-before":      regex += translator.before(args[i+1])
            elif arg == "-after":       regex += translator.after(args[i+1])
            elif arg == "-notbefore":   regex += translator.notbefore(args[i+1])
            elif arg == "-notafter":    regex += translator.notafter(args[i+1])
            elif arg == "-nograb":      regex += translator.nograb(args[i+1])
            elif arg == "-group":       regex += translator.group(args[i+1])
            elif arg == "-groupref":    regex += translator.groupref(args[i+1])
            elif arg == "-or":          regex += translator.rengex_or(args[i+1], args[i+2])
            i += extra_args
        elif arg in character_classes:
            regex += character_classes[arg]
        else:
            print(f"Error in parsing arguments, invalid argument {arg}")
            print("For help use the -h flag")
            exit(0)
        i += 1
    return regex

if len(sys.argv) > 2:
    print(f"One argument expected, received {len(sys.argv) - 1}")
    print("Please pass all arguments inside of single quotes to avoid shell expansion")
    exit(0)

input = sys.argv[1]
args = input.split(" ")

if args == "-h": print("Help message here")
print(f"Your REGEX is: {parse(args)}")
