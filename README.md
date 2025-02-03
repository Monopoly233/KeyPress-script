# Keyboard Auto Press Script

This Python script automates key presses in response to a user-defined key press event.

## Features
- Waits for the user to press a specified key.
- Repeatedly presses and releases the key a set number of times.
- Runs in an infinite loop, waiting for the next key press.

## Prerequisites
- Python 3.x
- Install the `keyboard` module if not already installed:
  ```bash
  pip install keyboard
  ```

## Usage
1. Modify the script variables if needed:
   - `key_to_hold`: The key that triggers the automated key presses (default: `'j'`).
   - `output_count`: The number of times the key is pressed per activation (default: `20`).
   - `output_interval`: Time delay between each key press in seconds (default: `0.00001`).
2. Run the script:
   ```bash
   python script.py
   ```
3. Press the specified key (`'j'` by default), and the script will simulate the key press sequence.
4. The script will wait for the next key press to repeat the process.

## Example
If `key_to_hold = 'j'`, `output_count = 20`, and `output_interval = 0.00001`, pressing `j` will trigger:
```
j j j j j j j j j j j j j j j j j j j j
```
And then wait for the next `j` press to repeat.

## Notes
- Ensure the script has the necessary permissions to simulate key presses.
- Running this script with very small intervals might cause high CPU usage.
- The script runs indefinitely until manually stopped (`Ctrl + C`).

## License
This script is free to use and modify for any personal or commercial projects.

