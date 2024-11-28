import time
import pyautogui
import tkinter as tk

def screenshot_the_display():
    title = int(round(time.time()*1000))
    title = f'screenshots/{title}.png'
    # title = "D:/Screenshots/{title}"  # file path
    shot = pyautogui.screenshot(title)
    shot.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command=screenshot_the_display
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text='Quit',
    command=quit
)
close.pack(side=tk.RIGHT)

root.mainloop()