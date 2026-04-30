# Password Maker

Generates a random password using letters, symbols, and numbers.

## How it works

1. User selects option 1 (Create Password) or 2 (Exit)
2. Enter desired password length
3. Program randomly picks unique characters from all available sets
4. Password is displayed with no repeating characters

## Run

```bash
python main.py
```

## Example

========= Welcome To Password Maker Program =========

Select Option: 

        1) Create Password

        2) Exit
Your Option: 1

Enter your password length: 8


Your password: ^"H7BPrS


=====================================================


Select Option:

        1) Create Password

        2) Exit

Your Option: 2


Program Closed

## Technical Note

Uses `random.sample()` for unique characters (no repeats).

`string.ascii_letters` provides both uppercase and lowercase.

Validates length to prevent `sample()` errors.

## Dependencies

None (uses only Python built-in modules)