# Countdown Timer

A simple countdown timer that takes hours, minutes, and seconds as input.

## How it works

1. User chooses to start timer (Y) or exit (N)
2. Enters hours, minutes, and seconds
3. Program converts everything to total seconds
4. Counts down second by second
5. Displays "TIMER ENDED" when done

## Run

```bash
python main.py
```

## Example

Welcome To Timer Program

Do you want to start timer? [Y/N]: Y

Enter hour: 0

Enter minutes: 0

Enter seconds: 3

Timer starts now...

Time remaining: 3 seconds

Time remaining: 2 seconds

Time remaining: 1 seconds

TIMER ENDED!

## Technical Note

`time.sleep(1)` creates a 1-second delay between each countdown step
Screen clearing works on Windows (`cls`) and Mac/Linux (`clear`)

## Dependencies

None (uses only Python built-in modules)
