# Palindrome Checker

A simple program that checks if a word or phrase is a palindrome (reads the same forwards and backwards).

## How it works

1. Takes input from user
2. Converts it to lowercase (so "Radar" and "radar" are both palindromes)
3. Reverses the string using [::-1]
4. Compares original with reversed version
5. Prints "Yes" if palindrome, "No" if not

## Run
```bash

python main.py
```

## Example

Enter your string to check: radar

Yes

Enter your string to check: hello

No

## Note

This version only works for single words without spaces or punctuation.

## Technical Note

Uses Python's string slicing `[::-1]`:
- Step `-1` reverses the string

## Dependencies

None (uses only Python built-in modules)