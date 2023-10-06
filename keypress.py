import keyboard
import time

# 设置按住的键位
key_to_hold = 'j'

# 设置连续输出次数
output_count = 20

# 设置连续输出的时间间隔（秒）
output_interval = 0.00001

# 提示用户开始
print(f"按下键位'{key_to_hold}'后，将连续输出{output_count}次。")
keyboard.wait(key_to_hold)

while True:
    # 开始按住键位并连续输出
    keyboard.press(key_to_hold)
    for i in range(output_count):
        keyboard.press_and_release(key_to_hold)
        time.sleep(output_interval)
    keyboard.release(key_to_hold)

    print(f"按住键位'{key_to_hold}'并连续输出{output_count}次完成！")
    print("等待下一次按下键位...")
    keyboard.wait(key_to_hold)
