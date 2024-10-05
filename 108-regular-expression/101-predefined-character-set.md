# Predefined character sets (class).

- `\w`: - Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`
- `\W`: matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`

- `\d`: Matches any decimal digit; thisis equivalent to the class `[0-9]`.
- `\D`: Matches any non-digit character, this is equivalent to the class `[^0-9]`
- `\s`: Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.
- `\S`: Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.

These sequences can be included inside a character class. For example, `[\s,.]` is a character class that will match any whitespace character, or `','` or `'.'`.

- `\A`: Matches only at the start of the string.
    - Work similar to `^` when not in `re.MULTILINE` mode.
    - [Usage](104-difference-backslash-a-and-anchor.ipynb)

- `\Z`: Matches only at the end of string.

- `\b`: Word boundary.
    - This is a zero-width assertion that matches only at the begining or end of the word. 
    - A word is defined as a sequence of alphanumeric characters, so the word is indicated by whitespace or a non-alphanumeric character.
    - It won't match when it's contained inside another word.

- `\B`: Another zero-width assertion.
    - This is the opposite of `\b`, only matching when the current position is not at the word boundary.