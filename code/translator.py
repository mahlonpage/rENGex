from store import character_classes, flags, escape_characters

# Parse the arguments and return the regex
def parse(args):
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
            elif arg == "-)":                       error("No opening parenthesis")
            elif arg == "-(" or "-nograb(":
                j = i
                final = None
                while j < len(args):
                    if args[j] == "-)": final = j
                    j += 1
                if not final: error("No closing parenthesis")
                if arg == "-(": regex += group(args[i+1:final])
                else: regex += nocapture(args[i+1:final])
                i = final
            i += extra_args
        elif arg in character_classes:
            regex += character_classes[arg]
        else:
            print("For help use the -h flag")
            error(f"Could not parse, invalid argument {arg}")
        i += 1
    return regex

# Append a literal string to the regex
def lit(literal):
    return escape(literal)

# Generate a [] in statement from a comma separated list of characters, character classes, and ranges.
def rengex_in(options):
    options = options.split(",")
    res = "["
    for option in options:

        # If it is a character class, substitute it.
        if option in character_classes:

            # . is not allowed inside an in statement
            if character_classes[option] == '.': error(f"Error: {option} is not allowed inside an in statement")
            res += character_classes[option]

        # If it is a range, substitute it.
        elif option[:6].lower() == 'range:': res += rengex_range(option[6:])
        # All non range/character classes must be one character.
        elif not len(option) == 1: error(f"Error: invalid input into in statement. Must be character, char class, or range. Invalid input: {option}")
        else: res += escape(option)
    res += "]"
    return res

# Same as rengex_in except we want to exclude these characters.
def notin(options):
    res = rengex_in(options)
    res = res[0] + "^" + res[1:]
    return res

# Creates a non capturing group. Created with "-nograb(" and "-)"
def nocapture(options):
    return "(?:" + parse(options) + ")"

# Recursively parses group statements.
def group(contents):
    return "(" + parse(contents) + ")"

# Handles ranges in form of range:x-y
def rengex_range(items):
    items = items.split("-")
    if len(items) != 2: error("Invalid input into range statement, must be two characters separated by a dash")
    if items[0] > items[1]: error(f"Invalid range statement input, {items[0]} not less than {items[1]}")
    items[0] = escape(items[0])
    items[1] = escape(items[1])
    return f"{items[0]}-{items[1]}"

# Escapes a string by adding \ as needed before escape characters.
def escape(characters):
    res = ""
    for character in characters:
        if character in escape_characters: res += "\\"
        res += character
    return res

# Easy errors
def error(message):
    print(message)
    exit(0)
