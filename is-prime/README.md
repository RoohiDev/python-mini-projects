# Prime Number Checker

A simple program that checks if a number is prime, composite, or neither.

## How it works

1. Takes a number from user
2. If number is less than 2 → "neither prime nor composite"
3. Checks divisibility from 2 to square root of the number
4. If any divisor found → number is composite
5. If no divisor found → number is prime

## Run

```bash
python main.py
```

## Example

Enter your number: 7

7 is prime

Enter your number: 10

10 is composite

Enter your number: 1

1 is neither prime nor composite

Enter your number: abc

Please enter a numeric value!

## Technical Note

Uses Python's `for-else` syntax:
- `else` runs only if loop finds no divisor

## Dependencies

None (uses only Python built-in modules)