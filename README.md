# rENGex

rENGex is a simple english-regex hybrid language that compiles to regular expressions.
It is designed to be easy to read and write, and to be a stepping stone for learning regex.

I built this project with the goal of creating a beginner-friendly way of learning and using regex. Along the way this project has refined my knowledge of the nuances of regex and given me a chance to practice parsing and scripting.

https://github.com/mahlonpage/rENGex/assets/90529561/fbdf101a-011d-428a-a4d3-a93f0279e4ea

## Setup
Conveniently, this program comes with a setup script.

1. Open a terminal and navigate to this repository
2. Run ./deploy.sh
3. Restart your terminal
4. Run the program in the command line: `regex '<rENGex input>`

Note: this only works for Unix-based shells.

## Usage

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

## Examples
