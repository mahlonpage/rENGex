escape_characters = set("[](){}^$*+?|\\.")

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
    "-nograb(": 1,
    "-(": 1,
    "-)": -1
}