# Class containing relevant substitutions and information for rengex parsing.

# Characters that need to be escaped in a regex.
escape_characters = set("[](){}^$*+?|\\.")

# Valid digits.
digits = set("0123456789")

# Valid quantifier inputs in our language. This is all digits and - and +
valid_quantifier_inputs = set("+-0123456789")

# This dictionary contains all non-flag word straight substitutions for our language.
character_classes = {
    "start": "^",
    "end": "$",
    "beginning": "\A",
    "ending": "\Z",
    "digit": "\d",
    "nondigit": "\D",
    "letter": "\w",
    "nonletter": "\W",
    "whitespace": "\s",
    "nonwhitespace": "\S",
    "character": ".",
    "punctuation": "[:punct:]"
}

# This dictionary contains all flag words and the number of extra tokens they consume when you
# encounter them.
# For example, -lit eats the next token as the literal string to pass in.
# Note: -) should never need this value so it is set to -1 for error-detection.
# -nograb( and -( consume variable amounts of tokens so they handle their own incrementing in translator.py
flags = {
    "-nocase": 0,
    "-lit": 1,
    "-in": 1,
    "-notin": 1,
    "-nograb(": 0,
    "-(": 0,
    "-)": -1,
    "-groupref": 1
}
