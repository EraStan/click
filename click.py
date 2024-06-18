import pyautogui
import schedule
import time
from datetime import datetime
import tkinter as tk
import http.client
import time
import os
task_completed = False


def get_webserver_datetime(website):
    try:
        conn = http.client.HTTPConnection(website)
        conn.request("GET", "/")
        # 获取响应
        rsp = conn.getresponse()
        # 获取http头date部分
        timestamp = rsp.getheader('date')

        # 将GMT时间转换成北京时间
        ltime = time.strptime(timestamp[5:25], "%d %b %Y %H:%M:%S")
        bjtime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)

        date = "%u-%02u-%02u" % (bjtime.tm_year, bjtime.tm_mon, bjtime.tm_mday)
        tm = "%02u:%02u:%02u" % (bjtime.tm_hour, bjtime.tm_min, bjtime.tm_sec)
        dt = date + " " + tm
        return dt
    except:
        return None
def get_position():
    while True:
        current_x, current_y = pyautogui.position()
        print("当前鼠标位置：", current_x, current_y)
        time.sleep(1)
def click():
    print("定时任务开始", datetime.now())

    #print(get_webserver_datetime('www.njupt.edu.cn'))

    #测试位置
    #pyautogui.click(236, 506)

    #确认预约
    pyautogui.click(1380, 877)

    print("定时任务完成",datetime.now())
    global task_completed
    task_completed = True
def click_schedule():
    print("正在执行...")
    global task_completed
    schedule.every().day.at("12:00:00").do(click)
    while not task_completed:
        schedule.run_pending()

        #time.sleep(0.1)


if __name__ == '__main__':
    #get_position()
    click_schedule()

    # print("任务开始", datetime.now())
    # print(get_webserver_datetime('www.njupt.edu.cn'))
    # print("任务结束", datetime.now())