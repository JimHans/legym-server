# -*- coding: UTF-8 -*-

import schedule,time  # 引入schedule模块

import sys

import legym

from datetime import datetime

'''def automation_for_debug():
    if len(sys.argv) != 2:
        raise Exception("arguments not provided")
    username, password, distance, activity = sys.argv[1].split("#")

    user = legym.login(username, password)
    print(f"{user=}")

    running_result = user.running(float(distance))
    print(f"{running_result=}")

    register_result = user.register(name=activity)
    print(f"{register_result=}")

    sign_result = user.sign()
    print(f"{sign_result=}")
'''

def automation_register():
    if len(sys.argv) != 2:
        raise Exception("arguments not provided")
    username, password = sys.argv[1].split("#")

    f = open("ServerRuntime.log", "a+") # 打开文件写入日志
    print("Login...", end="")
    f.writelines(str(time.localtime()[0])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[2])+"-")
    f.writelines(str(time.localtime()[3])+"-"+str(time.localtime()[4])+"-"+str(time.localtime()[5])) # 写入时间戳
    f.writelines('Login...')
    user = legym.login(username, password)
    print("success")
    f.writelines('success\n')

    # print("SkipRunning...", end="")

    '''actual_distance, success = user.running(float(distance))
    if success:
        print(f"{actual_distance} km")
    else:
        print("failed")
    '''

    dayOfWeek = datetime.now().isoweekday()
    # judge week System
    if(dayOfWeek == 1): dayOfWeek_CN = "一"
    elif(dayOfWeek == 2): dayOfWeek_CN = "二"
    elif(dayOfWeek == 3): dayOfWeek_CN = "三"
    elif(dayOfWeek == 4): dayOfWeek_CN = "四"
    elif(dayOfWeek == 5): dayOfWeek_CN = "五" 
    elif(dayOfWeek == 6): dayOfWeek_CN = "六"
    else: dayOfWeek_CN = "天"
    activity1 = "第三空间周"+dayOfWeek_CN+"清水河校区体育场"
    activity2 = "第三空间周"+dayOfWeek_CN+"清水河校区综训馆"
    print("Registering "+activity1+"...", end="")
    f.writelines("Registering "+activity1+"...")
    _, success, _ = user.register(name=activity1)
    if success:
        print("success")
        f.writelines("success\n")
    else:
        print("failed")
        f.writelines("failed\n")
    
    print("Registering "+activity2+"...", end="")
    f.writelines("Registering "+activity2+"...")
    _, success, _ = user.register(name=activity2)
    if success:
        print("success")
        f.writelines("success\n")
    else:
        print("failed")
        f.writelines("failed\n")
    f.close()


def automation_sign():
    if len(sys.argv) != 2:
        raise Exception("arguments not provided")
    username, password = sys.argv[1].split("#")

    f = open("ServerRuntime.log", "a+") # 打开文件写入日志
    print("Login...", end="")
    f.writelines(str(time.localtime()[0])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[2])+"-")
    f.writelines(str(time.localtime()[3])+"-"+str(time.localtime()[4])+"-"+str(time.localtime()[5]))  # 写入时间戳
    f.writelines('Login...')
    user = legym.login(username, password)
    print("success")
    f.writelines('success\n')

    print("Signing...", end="")
    results = user.sign()
    if(results[1] == True):print("success")
    else : print("failed")
    print(results)
    f.write(str(results)+"\n")
    # for result in results:
    #     if result[1]:
    #         print("success")
    #     else:
    #         print("failed")
    f.close()



if __name__ == "__main__":
    f = open("ServerRuntime.log", "a+") # 打开文件写入日志
    f.writelines(str(time.localtime()[0])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[2])+"-")
    f.writelines(str(time.localtime()[3])+"-"+str(time.localtime()[4])+"-"+str(time.localtime()[5]))
    f.writelines("系统启动\n")
    f.close()

    schedule.every().day.at("02:03").do(automation_register)# 报名活动
    schedule.every().day.at("17:00").do(automation_sign)# 签到
    schedule.every().day.at("18:35").do(automation_sign)# 二次签到
    while(True):
        # 启动服务
        schedule.run_pending()
        time.sleep(1)
