escape_characters = set("[](){}^$*+?|\\.")

digits = set("0123456789")

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

flags = {
    "-nocase": 0,
    "-lit": 1,
    "-in": 1,
    "-notin": 1,
    # -nograb( and -( handle their own incrementing so they add 0 by default.
    "-nograb(": 0,
    "-(": 0,
    "-)": -1,
    "-groupref": 1
}