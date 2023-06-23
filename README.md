# rENGex

Regex can be hard, especially for beginners. This project serves as a middle-language between English and Regex which can be used to generate regular expressions.

Setup:

1. Clone this repository
2. Open a terminal and navigate to the repository
3. Run ./deploy.sh
4. Restart your terminal
5. Now type: regex '\<input>'

Characters
\d - digit
\w - letter
\s - whitespace
\D - not digit
\W - not letter
\S - not whitespace
.  - character (except linebreak)
[:punct:] - punctuation

Quantifiers
+     - 1+
{x}   - x
{x,y} - x-y
{x,}  - x+
*     - 0+
?     - if 0-1, use this
example: from 1234
\d{2,4} will return 1234
\d{2,4}? will return 12

Logic
|  - -OR
() - -GROUP
\1 - contents of group 1 r(\w)g\1x = regex
(?: ) - non capturing group

White-Space
\t - tab
\r - return
\n - newline
\N - non-newline

Character Classes
[...] - one of in bracket
[x-y] - in range x-y
[^x]  - not x
[^x-y]- not in range x-y

Anchors/Boundaries
^ - start
$ - end
\A - beginning
\Z - ending
\b - word boundary (just one side has letter, num, _)
\B - not a boundary

Inline Modifiers
(?i) - case-insensitive
(?s) - let's . match \n
(?m) - match beginning and end every line

Lookarounds
(?= )  - Positive Lookahead
(?<= ) - Positive lookbehind
(?! )  - Negative lookahead
(?<! ) - Negative Lookbehind