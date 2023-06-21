import translator
import sys
from store import flags, character_classes

if len(sys.argv) > 2:
    print(f"One argument expected, received {len(sys.argv) - 1}")
    print("Please pass all arguments inside of single quotes to avoid shell expansion")
    exit(0)

input = sys.argv[1]
args = input.split(" ")
regex = ""

if args == "-h": print("Help message here")

i = 0
while i < len(args):
    arg = args[i]
    if arg in flags:
        extra_args = flags[arg]
        if   arg == "-nocase":      regex = translator.nocase(regex)
        elif arg == "-lit":         regex = translator.lit(regex, args[i+1])
        elif arg == "-in":          regex = translator.rengex_in(regex, args[i+1])
        elif arg == "-notin":       regex = translator.notin(regex, args[i+1])
        elif arg == "-before":      regex = translator.before(regex, args[i+1])
        elif arg == "-after":       regex = translator.after(regex, args[i+1])
        elif arg == "-notbefore":   regex = translator.notbefore(regex, args[i+1])
        elif arg == "-notafter":    regex = translator.notafter(regex, args[i+1])
        elif arg == "-nograb":      regex = translator.nograb(regex, args[i+1])
        elif arg == "-group":       regex = translator.group(regex, args[i+1])
        elif arg == "-groupref":    regex = translator.groupref(regex, args[i+1])
        elif arg == "-or":          regex = translator.rengex_or(regex, args[i+1], args[i+2])
        i += extra_args
    elif arg in character_classes:
        regex += character_classes[arg]
    else:
        print(f"Error in parsing arguments, invalid argument {arg}")
        print("For help use the -h flag")
        exit(0)
    i += 1

print(f"Your REGEX is: {regex}")

# Rengex:
# Flags:
#     -lit             | -lit string                          | 1
#     -in/RANGE        | -in a,b,c,letter,digit,RANGE(A-Z)    | 1
#     -notin/RANGE     | -notin a,b,c,RANGE(A-Z)              | 1
#     -nocase          | -nocase                              | 0
#     -multiline       | -multiline                           | 0
#     -before          | -before ??                           | 1
#     -after           | -after ??                            | 1
#     -notbefore       | -notbefore ??                        | 1
#     -notafter        | -notafter ??                         | 1
#     -nograb          | -nograb ??                           | 1
#     -or              | -or opt1 opt2                        | 2

# Text:
#     start                                                   | ^  (line)
#     end                                                     | $  (line)
#     beginning (per line)                                    | \A (string)
#     ending (per line)                                       | \Z (string)
#     digit(s)                                                | \d
#     letter(s)                                               | \w
#     whitespace(s)                                           | \s
#     character(s)                                            | .
#     punctuation                                             | [:punct:]
#     1... (denoting number times)                            |
#     GROUP                                                   |