from time import sleep
import pyautogui
import csv
import random
import sys

pyautogui.FAILSAFE = True

results = []
with open("tumbzilla_labels.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)  # change contents to floats
    for row in reader:  # each row is a list
        results += row  # adds row to array

# Select the first application in the taskbar (should be messenger)
pyautogui.hotkey('win', '1')

# find the message input field (messenger needs to be in dark mode)
s = pyautogui.locateOnScreen('type.png', confidence=0.75)

if s is None:
    # with night light mode (messenger needs to be in dark mode)
    s = pyautogui.locateOnScreen('type2.png', confidence=0.75)

# move mouse to center of the message input field
if s is not None:
    pyautogui.moveTo((int(s[0]) + int(s[2]) // 2),
                     (int(s[1]) + int(s[3]) // 2))
else:
    sys.exit("The inputfield was not found")

pyautogui.click()  # click the messenger input field

# randomly select how many messages will be sent
the_range = random.randint(1, 20)

# prints how many messages will be sent
print(f'Number of lines, that will be printed: {the_range}')

for i in range(the_range):
    pyautogui.write(results[random.randint(0, len(results))],
                    interval=(random.randint(1, 5) / 100))  # chooses random message to send from array and types it out with random random interval between letters for each message
    pyautogui.press('enter')  # sends message
    print(i + 1)  # shows what line you are on
    # wait for a random period of time to not trigger messenger suspension for botting
    sleep(random.randint(0, 3))


print('END')
