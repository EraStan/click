import pyautogui
import time
import tkinter as tk
from threading import Thread
import schedule
from datetime import datetime

get_task_completed = False
task_completed = False

def get_position():
    while not get_task_completed:
        current_x, current_y = pyautogui.position()
        position_label.config(text=f"当前鼠标位置：{current_x}, {current_y}")
        time.sleep(0.5)

def start_getting_position():
    global get_task_completed
    get_task_completed = False
    get_position_thread = Thread(target=get_position)
    get_position_thread.daemon = True
    get_position_thread.start()

def stop_getting_position():
    global get_task_completed
    get_task_completed = True

def click():
    position_label.config(text=f"定时任务开始：{datetime.now()}")
    print("定时任务开始", datetime.now())
    pyautogui.click(236, 506)
    print("定时任务完成", datetime.now())
    global task_completed
    task_completed = True

def click_schedule():
    global task_completed
    schedule.every().day.at("21:58:30").do(click)
    while not task_completed:
        schedule.run_pending()
        position_label.config(text=f"当前时间：{datetime.now()}")
        time.sleep(1)

def start_click_schedule():
    click_schedule_thread = Thread(target=click_schedule)
    click_schedule_thread.daemon = True
    click_schedule_thread.start()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("获取鼠标坐标")
    root.geometry("600x400")

    # 创建一个按钮，用于启动获取坐标功能
    start_button = tk.Button(root, text="开始获取坐标", command=start_getting_position)
    start_button.pack(pady=10)

    # 创建一个按钮，用于停止获取坐标功能
    stop_button = tk.Button(root, text="停止获取坐标", command=stop_getting_position)
    stop_button.pack(pady=10)

    # 创建一个标签，用于显示当前鼠标位置
    position_label = tk.Label(root, text="当前鼠标位置：")
    position_label.pack(pady=10)

    # 创建一个按钮，用于开启定时点击任务功能
    schedule_button = tk.Button(root, text="开始定时点击任务", command=start_click_schedule)
    schedule_button.pack(pady=10)

    # 创建一个标签，用于显示时间完成
    position_label = tk.Label(root, text="")
    position_label.pack(pady=10)

    # 运行主循环
    root.mainloop()
