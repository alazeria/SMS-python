import os
import time

import numpy

# 全局变量
passwd = 'root'
info = list()


def global_initialization():
    boost()


# 登录
def login():
    username = 'root'
    count = 0
    print('请登录 >>>>>>>>>')
    while True:
        user = input('登录名：')
        pwd = input('密码：')
        if user == username and pwd == passwd:
            print('【登录成功！欢迎登录！】')
            break
        else:
            count += 1
            print('【密码错误！登录失败！】', count)
            if count % 3 == 0:
                print('【密码错误次数过多，请等待60秒后再试！】')
                time.sleep(60)


# 底层菜单
def boost():
    while True:
        print("--—--请选择系统功能--—--")
        print("1-登录")
        print("0-退出系统")
        print("--—---------------—--")
        user_numb = input("请输入功能序号：")
        user_numb = user_numb
        if user_numb == '1':
            login()
            os.system('pause')
            main_page()
        elif user_numb == '0':
            print("【退出成功！】")
            break
        else:
            print("输入有误，请重新输入！")
            os.system('pause')


# 功能菜单
def main_page():
    while True:
        print("--—--请选择系统功能--—--")
        print("1-添加学生信息")
        print("2-修改学生信息")
        print("3-删除学生信息")
        print("4-查询指定学生信息")
        print("5-查询所有学生信息")
        print("6-删除所有学生信息")
        print("7-修改root密码")
        print("8-保存学生信息到文件（students.npy)")
        print("9-从文件中读取数据（students.npy)")
        print("0-退出登录")
        print("--—---------------—--")
        user_numb = input("请输入功能序号：")
        user_numb = user_numb
        if user_numb == '1':
            add_info()
            os.system('pause')
        elif user_numb == '2':
            modify_info()
            os.system('pause')
        elif user_numb == '3':
            delete_info()
            os.system('pause')
        elif user_numb == '4':
            query_info()
            os.system('pause')
        elif user_numb == '5':
            query_allinfo()
            os.system('pause')
        elif user_numb == '6':
            delete_allinfo()
            os.system('pause')
        elif user_numb == '7':
            change_the_root_password()
            os.system('pause')
        elif user_numb == '8':
            save()
            os.system('pause')
        elif user_numb == '9':
            load()
            os.system('pause')
        elif user_numb == '0':
            print("【已登出！】")
            break
        else:
            print("输入有误，请重新输入！")
            os.system('pause')


# 1-添加学生信息
def add_info():
    global info
    s_id = input("请输入学号：")
    for i in info:
        if s_id == i["id"]:
            print("【此用户已存在，请勿重复添加】")
            return
    s_name = input("请输入姓名：")
    s_tel = input("请输入电话；")

    info_dict = dict()
    info_dict["id"] = s_id
    info_dict["name"] = s_name
    info_dict["tel"] = s_tel

    info.append(info_dict)
    print("【添加成功！】")


# 2-修改学生信息
def modify_info():
    global info
    modify_id = input("请输入您修改的学生学号：")
    for i in info:
        if modify_id == i["id"]:
            print(i)
            info.remove(i)
            s_id = input("请重新输入学号：")
            s_name = input("请重新输入姓名：")
            s_tel = input("请重新输入电话；")
            info_dict = dict()
            info_dict["id"] = s_id
            info_dict["name"] = s_name
            info_dict["tel"] = s_tel

            info.append(info_dict)
            print("【修改成功！】")
            break
    else:
        print("【该学生不存在！】")


# 3-删除学生信息
def delete_info():
    global info
    del_id = input("请输入您删除的学生学号：")
    for i in info:
        if del_id == i["id"]:
            info.remove(i)
            print("【删除成功！】")
            break
    else:
        print("【该学生不存在！】")


# 4-查询指定学生信息
def query_info():
    query_id = input("请输入您要查询的学生学号：")
    for i in info:
        if query_id == i["id"]:
            print(i)
            print("【查询成功！】")
            break
    else:
        print("【该学生不存在！】")


# 5-查询所有学生信息
def query_allinfo():
    print(*info, sep='\n')
    print("【已查出所有信息！】")


# 6-删除所有学生信息
def delete_allinfo():
    global info
    i_want_delete_allinfo = input("你真的想要这么做吗？删除所有学生信息请输入'root'")
    if i_want_delete_allinfo == 'root':
        info = list()
        print("【删除成功！】")


# 7-修改root密码
def change_the_root_password():
    global passwd
    print('请输入原密码 >>>>>>>>>')
    pwd = input('原密码：')
    if pwd == passwd:
        print('请输入新密码 >>>>>>>>>')
        passwd = input('新密码：')
    else:
        print('【密码错误！】')


# 8-保存学生信息到文件（students.npy)
def save():
    numpy.save('students.npy', numpy.array(info))
    print("【存储成功！】")


# 9-从文件中读取数据（students.npy)
def load():
    global info
    try:
        a = numpy.load('students.npy', allow_pickle=True)
        info = a.tolist()
        print("【读取成功！】")
    except:
        print("【还没有储存数据！】")  # 打开失败，文件不存在说明没有数据保存



# main()
global_initialization()
