# Predefined character sets.

- `\w`: - Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`
- `\W`: matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`

- `\d`: Matches any decimal digit; thisis equivalent to the class `[0-9]`.
- `\D`: Matches any non-digit character, this is equivalent to the class `[^0-9]`
- `\s`: Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.
- `\S`: Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.

These sequences can be included inside a character class. For example, `[\s,.]` is a character class that will match any whitespace character, or `','` or `'.'`.