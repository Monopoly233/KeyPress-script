import keyboard
import time

# set the pressed key
key_to_hold = 'j'

# set the number of time output
output_count = 20

#the interval between each output
output_interval = 0.00001

# remind the user
print(f"after press '{key_to_hold}'，will constant ouput {output_count} times")
keyboard.wait(key_to_hold)

while True:
    # press the key and release
    keyboard.press(key_to_hold)
    for i in range(output_count):
        keyboard.press_and_release(key_to_hold)
        time.sleep(output_interval)
    keyboard.release(key_to_hold)

    print(f"after press '{key_to_hold}'，will constant ouput {output_count} times")
    print("waiting for press...")
    keyboard.wait(key_to_hold)
