# Compilation flags



| Flag | Meaning |
|------|---------|
| IGNORECASE, I | Do case-insensitive matches. |
| ASCII, A | Make several escapes like `\w`, `\b`, `\s`, and `\d` match only on ASCII characters with the respective property. |
| DOTALL, S | Make `.` match any character, including newlines. |
| LOCALE, L | Do a locale-aware match. |
| MULTILINE, M | Multi-line matching, affecting `^` and `$`. |
| VERBOSE, X (for `extended`) | Enable verbose REs, which can be organized more clearnly and understandably. |


### re.I (re.IGNORECASE)

Perform case-insensitive matching; character class literal strings will match letter by ignoring class. For example, `[A-Z]` will match lowercase letters, too.

When the Unicode pattern `[a-z]` or `[A-Z]` are used in combination with the `IGNORECASE` flag, they will match the 52 ASCII letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless i), ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign). `Spam` will match `'Spam'`, `'spam'`, `'spAM'`, or `'ſpam'` (the latter is matched only in Unicode mode). This lowercase doesn't take the current locate into account, it will if you also set the LOCALE flag.


### re.L (re.LOCALE)

Make `\w`, `\W`, `\b`, `\B` and case-insensitive matching dependent on the current locale instaead of the Unicode database.