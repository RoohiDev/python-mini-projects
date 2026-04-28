# Guess The Number

A simple game where you guess a random number between 0 and 50.

## How it works

1. Program picks a random number between 0 and 50
2. Player guesses the number
3. Program gives hints: "go down" or "go up"
4. Game continues until player guesses correctly
5. Shows number of attempts at the end

## Run

```bash
python main.py
```

## Example

Welcome to "Guess The Number"


Enter your target number (0-50): 25

It's lower! go up!

Enter your target number (0-50): 40

It's bigger! go down!

Enter your target number (0-50): 35

You Win! Your attempts: 3

## Technical Note

Uses `random.randint()` to generate random number.
`while True` loop with `break` when guessed correctly.

## Dependencies

None (uses only Python built-in modules)