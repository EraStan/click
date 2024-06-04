import pyautogui
import schedule
import time
from datetime import datetime
import tkinter as tk

task_completed = False
def get_position():
    while True:
        current_x, current_y = pyautogui.position()
        print("当前鼠标位置：", current_x, current_y)
        time.sleep(1)
def click():
    print("定时任务开始", datetime.now())
    pyautogui.click(236, 506)
    print("定时任务完成",datetime.now())
    global task_completed
    task_completed = True
def click_schedule():
    print("正在执行...")
    global task_completed
    schedule.every().day.at("13:23:00").do(click)
    while not task_completed:
        schedule.run_pending()

        #time.sleep(0.01)

def button_click():
    print("按钮被点击了！")

# 创建窗口
root = tk.Tk()
root.title("带有按钮的界面")

# 创建按钮
button = tk.Button(root, text="点击我", command=button_click)
button.pack()

# 运行窗口


if __name__ == '__main__':
    #get_position()
    #click_schedule()
    root.mainloop()