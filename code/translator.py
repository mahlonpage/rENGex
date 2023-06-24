import store

# This file handles parsing and translating our english-regex hybrid language into a pure regex.
#
# Mahlon Page

# Parse the arguments and return the regex
def parse(args):
    regex = ""
    i = 0
    quantifier_pending = False
    quantifier = None
    while i < len(args):
        arg = args[i]
        if arg in store.flags:
            extra_args = store.flags[arg]
            if   arg == "-nocase":                  regex =  "(?i)" + regex
            elif arg == "-lit":                     regex += lit(args[i+1])
            elif arg == "-in":                      regex += rengex_in(args[i+1])
            elif arg == "-notin":                   regex += notin(args[i+1])
            elif arg == "-groupref":                regex += groupref(args[i+1])
            elif arg == "-)":                       error("No opening parenthesis")
            elif arg == "-(" or "-nograb(":
                # Figure out how many arguments are in the group, and parse them.
                # Find matching closing parenthesis.
                opening_parentheses = 0
                j = i
                final = None
                while j < len(args):
                    if args[j] == "-(" or args[j] == "-nograb(": opening_parentheses += 1
                    if args[j] == "-)":
                        opening_parentheses -= 1
                        if opening_parentheses == 0:
                            final = j
                            break
                    j += 1
                if not final: error("Imbalanced parentheses.")
                if arg == "-(": regex += group(args[i+1:final])
                else: regex += nocapture(args[i+1:final])
                # Increment i to the end of the group.
                i = final

            # Increment counter to represent all arguments eaten by this flag.
            i += extra_args

        elif arg in store.character_classes: regex += store.character_classes[arg]
        elif arg[0] in store.digits:
            quantifier_pending = True
            quantifier = numerical_quantifier(arg)
            i += 1
            continue
        else:
            print("For help use the -h flag")
            error(f"Could not parse, invalid argument {arg}")

        if quantifier_pending:
            regex += quantifier
            quantifier = None
            quantifier_pending = False

        # Increment to next argument
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
        if option in store.character_classes:

            # . is not allowed inside an in statement
            if store.character_classes[option] == '.': error(f"Error: {option} is not allowed inside an in statement")
            res += store.character_classes[option]

        # If it is a range, substitute it.
        elif option[:6].lower() == 'range:': res += rengex_range(option[6:])
        # All non range/character classes must be one character.
        elif not len(option) == 1: error(f"Error: invalid input into in statement. Must be character, char class, or range. Invalid input: {option}")
        elif option == '-': res += '\-' # - is a special character in an in statement only
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

# Reference a previously created group. Created with "-groupref" and a number.
def groupref(number):
    value = int(number)
    if value <= 0: error("Group references must be positive integers")
    return "\\" + number

# Handles ranges in form of range:x-y
def rengex_range(items):
    items = items.split("-")
    if len(items) != 2: error("Invalid input into range statement, must be two characters separated by a dash")
    if items[0] > items[1]: error(f"Invalid range statement input, {items[0]} not less than {items[1]}")
    items[0] = escape(items[0])
    items[1] = escape(items[1])
    return f"{items[0]}-{items[1]}"

# Handles the various possible range amounts.
def numerical_quantifier(arg):
    for character in arg:
        if character not in store.valid_quantifier_inputs: error(f"Invalid quantifier {arg}. Each character must be a +, -, or number.")

    if arg.count('-') > 1: error(f"Invalid quantifier {arg}. Too many dashes.")
    if arg.count('+') > 1: error(f"Invalid quantifier {arg}. Too many +s.")
    if arg.count('-') == 1 and arg.count('+') == 1: error(f"Invalid quantifier {arg}. Cannot have both a + and a -")
    if arg.find('+') != -1 and arg.find('+') != len(arg) - 1: error(f"Invalid quantifier {arg}. + must come at the end of quantifier.")

    if '+' not in arg and '-' not in arg: return '{' + arg + '}'
    if '+' in arg:
        if arg[0: len(arg) - 1] == '0': return '*'
        elif arg[0: len(arg) - 1] == '1': return '+'
        else: return '{' + arg[0: len(arg) - 1] + ',}'
    if '-' in arg and arg.find('-') == len(arg) - 1:
        return '{0,' + arg[0: len(arg) - 1] + '}'
    elif '-' in arg:
        numbers = arg.split('-')
        if int(numbers[0]) >= int(numbers[1]): error(f"Invalid quantifier {arg}. The first number must be greater than the second.")

        if int(numbers[0]) == 0 and int(numbers[1]) == 1: return '?'
        else: return '{' + numbers[0] + ',' + numbers[1] + '}'


# Escapes a string by adding \ as needed before escape characters.
def escape(characters):
    res = ""
    for character in characters:
        if character in store.escape_characters: res += "\\"
        res += character
    return res

# Easy errors
def error(message):
    raise Exception(message)
