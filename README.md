# Temperature Average Calculator

A Python script that collects temperature readings from user input and calculates the average, stopping when the user types "done".

## How it works
- Repeatedly asks for a temperature reading
- Keeps a running total and count of valid entries
- Type `done` to stop entering values
- Prints the average of all entered readings (or a message if none were entered)

## How to run
```bash
python temperature_average.py
```
Enter numbers one at a time, then type `done` when finished.

## What I learned
- Using `while True` with a `break` condition for input loops of unknown length
- Converting user input to a number with `float()`
- Handling the edge case of zero entries to avoid a division-by-zero error
