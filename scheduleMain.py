import schedule
import subprocess
import time
import threading
import random


def my_task():
    print("Task is running, time:"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    command = "python3 main.py"  # 需要后台运行的命令，这里以运行your_script.py为例
    run_command(command)


def run_command(cmd):
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



def run_scheduled_task():
    random_number = random.randint(10, 59)

    random_number_str = str(random_number)
    schedule.every().day.at("09:" + random_number_str ).do(my_task)  # 每天9点10分 - 9点59分 之间执行一次my_task
    print("下次执行时间 -》 09：" + random_number_str)

    while True:
        schedule.run_pending()
        time.sleep(1)  # 休眠1秒，以防止循环频繁占用CPU

def run_in_background():
    background_thread = threading.Thread(target=run_scheduled_task)
    background_thread.daemon = True  # 设置为守护线程，这样当主线程结束时，该线程也会结束
    background_thread.start()

if __name__ == "__main__":
    print("Program started. Running task in the background at 9:30 AM every day.")
    run_in_background()

    try:
        while True:
            time.sleep(1)  # 保持主程序运行
    except KeyboardInterrupt:
        print("Program terminated.")


