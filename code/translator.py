from store import character_classes, flags, escape_characters

def nocase(regex): return "(?m)" + regex

def lit(regex, literal):
    literal = escape(literal)
    regex += literal
    return regex

def rengex_in(regex, options):
    options = options.split(",")
    res = "["
    for option in options:
        if option in character_classes:
            if character_classes[option] == '.':
                print(f"Error: {option} is not allowed inside an in statement")
                exit(0)
            option = character_classes[option]

        elif option[:6].lower() == 'range:': option = rengex_range(option[6:])
        elif len(option) >= 1:
            print("Error: invalid input into in statement. Each comma separated input must be a character, or keyword")
            print(f"Invalid input: {option}")
            exit(0)
        res += option
    res += "]"
    regex += res
    return regex

def notin(regex, options):
    pass

def before(regex, options):
    pass

def after(regex, options):
    pass

def notbefore(regex, options):
    pass

def notafter(regex, options):
    pass

def nograb(regex, options):
    pass

def group(regex, contents):
    pass

def groupref(regex, id):
    pass

def rengex_or(regex, option1, option2):
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
