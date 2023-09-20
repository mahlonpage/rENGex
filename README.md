# rENGex

rENGex is a simple english-regex hybrid language that compiles to regular expressions through the rENGex Engine (this project!). The language is designed to be easy to read and write, and allows easy creation of complex regular expressions. Watch the demo below to see its magic in action!

https://github.com/mahlonpage/rENGex/assets/90529561/2ef4fd84-ac72-41bb-bd6a-2d2cdcd74536

## Setup
Conveniently, this program comes with a setup script.

1. Open a terminal and navigate to this repository
2. Run ./deploy.sh
3. Restart your terminal
4. Run the program in the command line: `regex '<rENGex input>'`

Note: this only works for Unix-based shells.

## Usage

To use: `python3 ./code/rENGex.py '<input>'` or `regex '<input>'`

For help run 'regex -h' or 'regex -help'

rENGex inputs are made up of three major components: quantifiers, substitutions, and flags. Notably, flags will consume the following arguments as part of it's translation. For example, a -groupref flag, references a group number and consumes the next input as that group number.

### Quantifiers
Before almost any term you may use a quantifier to specify how many matches of an item you would like to occur. You can input these in the formats:
| Quantifier | Explanation |
| ---------- | --------- |
| **\<number>**  | Expresses an exact number quantifier |
| **\<number>+** | Expresses a minimum number quantifier |
| **\<number>-** | Expresses a maximum number quantifier |
| **\<number>-\<number>** | Expresses a range quantifier |

Each of these methods can be used to express a quantity desired for the item which follows it.

### Substitutions

Substitutions are words which can be typed and they will be matched with any item of that type. For example inputting into the rENGex engine, `'digit'` will create a regex which matches with any digit.

We also have special substitutions, these functions are special in denoting the start or end of a line or string.

Substitutions:
| Keyword | Meaning |
| ------- | ------- |
| digit          | Matches any digit            |
| nondigit       | Matches any non-digit        |
| letter         | Matches any letter           |
| nonletter      | Matches any non-letter       |
| whitespace     | Matches any whitespace       |
| nonwhitespace  | Matches any non-whitespace   |
| space          | Matches a space              |
| character      | Matches any character        |
| wordedge       | Matches any edge between a word and a non-alphanumeric charcter |
| nonwordedge    | Matches any non wordedge     |

Special Substitutions:
| keyword | Meaning |
| ------- | ------- |
| start        |  Matches the start of a line. (more common)       |
| end          |  Matches the end of a line. (more common)         |
| beginning    |  Matches the beginning of a string. (less common) |
| ending       |  Matches the end of a string. (less common)       |

### Flags
Flags (with the exception of -nocase) are used to denote that the following tokens should be treated
differently and are to be consumed by the flag. Flags are denoted with a - before the flag name. Each flag
takes the number of words after it as denoted in the table.

"?" denotes special group flags. Groups can be of infinite size and match up until they find their corresponding group close flag.

| Flag | Input Items Consumed | Meaning | Example Usage | Matching strings |
| ---------- | -------------------- | ------- | ------- | ------------ |
| -nocase    | 0 | Makes the regex case-insensitive. Can be used anywhere, but only once.  | -nocase -lit a | 'a', 'A'
| -lit       | 1 | Takes the next token as a literal string to search for.      | -lit hello               | 'hello'
| -in        | 1 | Takes the next token as a list of characters to match.       | -in a,b,c,range:1-9      | 'a', 'b', 'c', '1', '3', '9'
| -notin     | 1 | Takes the next token as a list of characters to not match.   | -notin a,b,c,range:1-9   | 'z', 'g', '0'
| -nograb(   | ? | Takes everything until matching -) as a non-capturing group. | -nograb( character -)   | 'a', '@', 'G'
| -(         | ? | Takes everything until matching -) as a capturing group, which can be referenced with -groupref     | -( character -) digit    | '12', '^2', 'b8'
| -)         | 0 | Ends a capturing or non-capturing group.                     | -( -nograb( character -) digit -) | '12', '^2', 'b8'
| -groupref  | 1 | Takes the next token as a group number to match.             | -( character -) -lit hello -groupref 1         | 'ahelloa', '@hello@', '9hello9'

## Examples

See the below table for several examples of usage as well as demo/demo.txt for a few detailed examples.

| rENGex input | Regex | Example matches |
| --------------- | ----- | --------------- |
| 3+ letter | \w{3,} | 'the' 'dragon' 'eatery' 'RefineMent' 'rENGex'
| -nocase -lit hello | (?i)hello | 'hello' 'HELLO' 'hElLo'
| -( digit -) -( digit -) -lit - -groupref 2 -groupref 1 | (\d)(\d)-\2\1 | '11-11' '21-12' '12-21' '95-59' |
| -( 2 -nograb( -in range:A-H -in range:1-8 -) -) -lit | -groupref 1 | ((?:[A-H][1-8]){2})\|\1 | 'A3H4 | A3H4' 'B1B8 | B1B8' |
| -nocase 2-4 -in range:a-c,g | (?i)[a-cg]{2,4} | 'aB' 'gABc' 'abc' 'cGb' 'bC' 'CbAG' |
| 3- -notin letter | [^\w]{0,3} | '34(' '@#' '1~8' '' |
| start whitespace digit letter end | ^\s\d\w$ | ' 4l' ' 8j' ' 1D' |
| 5+ -in letter,digit 1+ whitespace 4 digit | [\w\d]{5,}\s+\d{4} | 'hello 1234' 'exampletext            5839'
| -lit rENGex space -lit is space -lit awesome! | rENGex is awesome! | 'rENGex is awesome!' |
