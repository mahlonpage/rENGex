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
    "space": " ",
    "wordedge": "\\b",
    "nonwordedge": "\B",
    "character": "."
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

wrong_num_arguments_message= """======rENGex======
Please pass all arguments inside of single quotes to avoid shell expansion
Usage: regex '<rENGex>'
For help please run: regex -h"""

help_message = """
==================== rENGex ====================
Created by: Mahlon Page

rENGex is a simple english-regex hybrid language that compiles to regular expressions.
It is designed to be easy to read and write, and to be a stepping stone for learning regex.

For clarification about regex syntax & term definitions, see this helpful resource: https://www.rexegg.com/regex-quickstart.html

Usage:
    Normal:                                         python3 rENGex.py '<your rENGex here>'
    For help:                                       python3 rENGex.py -h
    .rc file shortcut installed by deploy.sh:       regex '<your rENGex here>'

    Valid Substitutions:
        digit:          Matches any digit.                                  Example: digit
        nondigit:       Matches any non-digit.                              Example: nondigit
        letter:         Matches any letter.                                 Example: letter
        nonletter:      Matches any non-letter.                             Example: nonletter
        whitespace:     Matches any whitespace.                             Example: whitespace
        nonwhitespace:  Matches any non-whitespace.                         Example: nonwhitespace
        character:      Matches any character.                              Example: character
        punctuation:    Matches any punctuation.                            Example: punctuation

    Start/End:
        start:          Matches the start of a line. (more common)          Example: start character
        end:            Matches the end of a line. (more common)            Example: end character
        beginning:      Matches the beginning of a string. (less common)    Example: beginning digit
        ending:         Matches the end of a string. (less common)          Example: ending digit

    Quantifiers:
        Before any term you can use a quantifier which specifies how many times to match.
        You can input quantifiers in one of three forms:
        <digit>                 Matches exactly that many times.  Example: 3 letter
        <digit>+                Matches at least that many times. Example: 3+ letter
        <digit>-<digit>         Matches between that many times.  Example: 3-7 letter

    Flags:
        Flags (with the exception of -nocase) are used to denote that the following tokens should be treated
        differently and are a part of the flag. Flags are denoted with a - before the flag name. Each flag
        takes the number of words after it as denoted immediately after the flag name. "?" denotes that
        the number of tokens is limitless and ends when a matching -) flag is found.
        -nocase:   0   Makes the regex case-insensitive.                               Example: -nocase
        -lit:      1   Takes the next token as a literal string.                       Example: -lit hello
        -in:       1   Takes the next token as a list of characters to match.          Example: -in a,b,c,range:1-9
        -notin:    1   Takes the next token as a list of characters to not match.      Example: -notin a,b,c,range:1-9
        -nograb(:  ?   Takes everything until matching -) as a non-capturing group.    Example: -nograb() character -) digit
        -(:        ?   Takes everything until matching -) as a capturing group.        Example: -( character -) digit
        -):        0   Ends a capturing or non-capturing group.                        Example: -( character -) digit -)
        -groupref: 1   Takes the next token as a group number to match.                Example: -( character -) -groupref 1

    For example:
        The following rENGex does a simple email match:
            regex '1+ character -lit @ 1+ character -lit . 1+ character'

        The following rENGex matches strings which have some amount of the same character on each sides of a -
            regex '-( 1+ letter -) -lit - -groupref 1'

    For more examples, please visit: https://github.com/mahlonpage/rENGex
"""