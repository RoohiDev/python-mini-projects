# Guess Name Game

Computer tries to guess your name from a list.

## How it works

1. Computer shows a list of names
2. You have 3 seconds to pick a name in your mind
3. Computer guesses randomly from the list
4. Answer Y (yes) or N (no)
5. Computer removes wrong guesses and tries again
6. Continues until guessed correctly or list is empty

## Run

```bash
python main.py
```

## Example

Choose one of these names:

['Alice', 'Bob', 'Gabriel', ...]

Is your name Alice? [Y/N]: N

Oops! +_+ let me try again

Is your name Bob? [Y/N]: Y

I guessed right! ^_^

## Technical Note
Uses `random.choice()` for random guessing.
`time.sleep(3)` gives user time to think.
Input validation accepts Y/N/YES/NO.
Removes wrong guesses from copied list.

## Dependencies

None (uses only Python built-in modules)