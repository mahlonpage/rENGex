from store import character_classes, flags, escape_characters

# Parse the arguments and return the regex
def parse(args, no_limits=True):
    regex = ""
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in flags:
            extra_args = flags[arg]
            if   arg == "-nocase":                  regex =  "(?i)" + regex
            elif arg == "-lit":                     regex += lit(args[i+1])
            elif arg == "-in":                      regex += rengex_in(args[i+1])
            elif arg == "-notin":                   regex += notin(args[i+1])
            elif arg == "-before" and no_limits:    regex += lookbehind(args[i+1])
            elif arg == "-after" and no_limits:     regex += lookahead(args[i+1])
            elif arg == "-notbefore" and no_limits: regex += notlookbehind(args[i+1])
            elif arg == "-notafter" and no_limits:  regex += notlookahead(args[i+1])
            elif arg == "-nograb" and no_limits:    regex += nocapture(args[i+1])
            elif arg == "-group":                   regex += group(args[i+1])
            elif arg == "-groupref":                regex += groupref(args[i+1])
            elif arg == "-or" and no_limits:        regex += rengex_or(args[i+1], args[i+2])
            else: print(f"Error in parsing arguments, invalid flag {arg} inside of {args}")
            i += extra_args
        elif arg in character_classes:
            regex += character_classes[arg]
        else:
            print(f"Error in parsing arguments, invalid argument {arg}")
            print("For help use the -h flag")
            exit(0)
        i += 1
    return regex

# Append a literal string to the regex
def lit(literal):
    return escape(literal)

# Generate a [] in statement from a comma separated list of characters, character classes, and ranges.
def rengex_in(options):
    options = options.split(",")
    print(options)
    res = "["
    for option in options:
        # If it is a character class, substitute it.
        if option in character_classes:
            if character_classes[option] == '.': # . is not allowed inside an in statement
                print(f"Error: {option} is not allowed inside an in statement")
                exit(0)
            res += character_classes[option]

        # If it is a range, substitute it.
        elif option[:6].lower() == 'range:': res += rengex_range(option[6:])
        elif not len(option) == 1: # All non range/character classes must be one character.
            print("Error: invalid input into in statement. Each comma separated input must be a character, or keyword")
            print(f"Invalid input: {option}")
            exit(0)
        else:
            res += escape(option)
    res += "]"
    return res

# Same as rengex_in except we want to exclude these characters.
def notin(options):
    res = rengex_in(options)
    res = res[0] + "^" + res[1:]
    return res

def lookbehind(options):
    pass

# In reality, can contain any regex, however look behinds cannot, limiting scope since this is for simpler regex.
def lookahead(options):
    pass

def notlookahead(options):
    pass

def notlookbehind(options):
    pass

def nocapture(options):
    pass

def group(contents):
    pass

def groupref(id):
    pass

def rengex_or(option1, option2):
    pass

def rengex_range(items):
    items = items.split("-")
    if len(items) != 2:
        print("Error: invalid input into range statement. Must be two characters separated by a dash")
        print(f"Invalid input: {items}")
        exit(0)
    if items[0] > items[1]:
        print("Error: invalid input into range statement. First character must be less than second character")
        print("Use ASCII values, for basic charcters the order is: 0-9, then uppercase letters, then lowercase letters")
        print(f"Invalid input: {items}")
        exit(0)
    items[0] = escape(items[0])
    items[1] = escape(items[1])
    return f"{items[0]}-{items[1]}"

def escape(characters):
    res = ""
    for character in characters:
        if character in escape_characters: res += "\\"
        res += character
    return res
