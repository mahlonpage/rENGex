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
    #"-multiline": 0,
    "-lit": 1,
    "-in": 1,
    "-notin": 1,
    "-before": 1,
    "-after": 1,
    "-notbefore": 1,
    "-notafter": 1,
    "-nograb": 1,
    "-group": 1,
    "-groupref": 1,
    "-or": 2
}