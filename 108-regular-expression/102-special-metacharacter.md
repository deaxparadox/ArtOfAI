# Regular Expression Metacharacters

Here's a complete list of the metacharacters;

- `$`

### Repeating things
    - `*`
    - `+`
    - `?`
    - `{`
    - `}`

### Specifying Character class

- [`[]`](#square-brackets)
- `^`
- `.`
- `\`

- `|`
- `(`
- `)`


### Period (Dot)

It matches anything except a newline character, and there's an alternate mode (`re.DOTALL`) where it will match event a newline. `.` is often used where you want to match "any character".

### Anchor

- You can match the characters not listed within the class by *complementing* the set. This is indicated by including a `'^'` as the first character of the class. For example `[^5]` will match any character except `'5'`. If the caret appears elsewhere isn a character class, it does not have special meaning. For example: `[5^]` will match either a `'5'` or a `'^'`.


For example, if you wish to match the word `From` only at the begining of a line, th RE to use is `^From`.

```py
>>> print(re.search('^From', 'From Here to Eternity'))  
<re.Match object; span=(0, 4), match='From'>
>>>
>>> print(re.search('^From', 'Reciting From Memory'))
None
>>>
```

To match a literal `'^'`, use `\^`.


### Dollar

Matches at the end of the line, which is defined as either the end of the string, or any location followed by a newline character.

```py
>>>
>>> print(re.search('}$', '{block}'))    
<re.Match object; span=(6, 7), match='}'>
>>>
>>> print(re.search('}$', '{block} '))
None
>>>
>>> print(re.search('}$', '{block}\n'))  
<re.Match object; span=(6, 7), match='}'>
>>>
```

- To match a literal `'$'`, use `\$` or enclose it inside a character class, as in `[$]`.


### Star

- `'*'` specifies character can be matched zero or more times, instead of exactly once.
- For example, `ca*t` will match `'ct'` (0 `'a'` characters), `'cat'` (1 `'a'`), `'caat'` (2, `'a'`), `'caaat'` (3, `'a'`), and so forth.
- Repitions such as `*` are *greedy*, when repeating a RE, the matching engine will try to repeat it as many times as possible. If latter portions of the pattern don't match, the matching engine will then back up and try again with few repetitions.

### Plus

- `+` matches one or more times.
- `+` requires at least *one* occurence. 
- Example, `ca+t` will athc `'cat'` (1 `'a'`), `'caat'` (2, `'a'`), but won't match `'ct'`.

### Question Mark

- `?` matches either once or zero times.
- Example, `home-?brew` matches wither `'homebrew'` or `'home-brew'`.

### Curly Brackets

- `{m, n}` are most complicated quantifier, where *m* and *n* are decimal integers. This quantifiers means there must be at least *m* repetitions, at most *n*.
- For example, `a/{1,3}b` will match `'a/b'`, `'a//b'`, and `'a///b'`. It won't match `'ab'`, which has no slashes, or `'a////b'`, which has four.
- The simplest case `{m}` matches the preceeding item exactly `m` times. For example, `a/{2}b` will only match `'a//b'`.
- Quantifier `{0,}` is equivalent to `*`.
- Quantifier `{1,}` is equivalent to `+`.
- Quantifier `{0,1}` is equivalent to `?`.


### Square Brackets

- Used for specify the character class, which is a set of characters that you wish to match.
- Characters can be listedn individually, or a range of characters can be indicated by giving two characters and separating them by a `-`. Example, `[abc]` will match any of the characters `a`, `b`, and `c`; this is the same as `[a-c]`, which uses a range to express the same set of characters. 
- If you wanted to match only lowercase letters, your RE would be `[a-z]`.
- Metacharacters (except `\`) are not active inside classes. For example, `[akm$]` will match any of the characters `'a'`, `'k'`, `'m'`, and `'$'`; `'$'` is usually a metacharacter, but inside a character clas it's stripeed of its special nature.

### Backward Slash

- It's used to escape all the metacharacters so you can still match them in patterns; for example, if you need to match a `[` or `\`, you can precede them with a backslash to remove their special meaning: `\[` or `\\`.

- Some of the special seuqences beginning with `'\'` represent predefined sets of characters that are often usefull, such as  the set of digits, the set of letters, or the set of anything that isn't whitespace.

View all the predefined character sets [here](predefined-character-set.md)

### `|` "or" operation

Alternation, or the "or" operation. IF *A* and *B* are regular expressions. `A | B` will match any string that matches either *A* or *B*. `|` has very low precendence in order to make it work resonably when you're alternating multi-character strings. `Crow|Servo` will match either `'Crow'` or `'Servo'`, not `'Cro'`, a `'w'`, or an `'S'`, and `'servo'`.

Ot match a literal `'|'`, use `\|`, or enclose it inside a character class, as in `[|]`.


### `(` `)` "group" parentheses

Groups are marked by the `(`, `)` metacharacters. `(` and `)` have muc the same meaning as they do in mathemtical expressions; they group together the expressions contained inside them, and you can repeat the contents of a gruop with a quantifier , such as `*`, `+`, `?`, or `{m, n}`. For example, `(ab)*` will match zero or more repetitions of `ab`.

```py
>>>
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())  
(0, 10)
>>>
```