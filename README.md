# rENGex

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
+     - 1+ times
{x}   - x times
{x,y} - x-y times
{x,}  - x+ times
*     - 0+ times
?     - if 0-1 times, use this
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