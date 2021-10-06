import os
import sys
import time

import numpy

# 申明全局变量
# 全局初始root密码
root_passwd = 'root'
# 全局学生信息
info = list()
# 全局密码错误次数计数
passwd_count = 0
# 全局学生信息文件夹
folder0 = 'SMS'
# 全局缓存文件夹
folder1 = 'SMS-Cache'
# 全局学生信息文件名
student_filename = '%s\\students.npy' % folder0
# root密码文件
root_filename = '%s\\root' % folder0
# 全局缓存计数
cache_count = list()
# 全局缓存计数文件名
cache_count_filename = '%s\\cache_count.npy' % folder1
# 全局缓存文件名
cache_filename = '%s\\cache%s.npy' % (folder1, len(cache_count))


# 全局初始化
def global_initialization():
    global cache_count
    global cache_filename
    global root_passwd
    # 创建文件夹
    if not os.path.exists(folder0):
        os.mkdir(folder0)
    if not os.path.exists(folder1):
        os.mkdir(folder1)
    # 创建文件
    if not os.path.exists(cache_count_filename):
        f = open(cache_count_filename, "x")
        f.close()
    if not os.path.exists(root_filename):
        f = open(root_filename, "x")
        f.write(str(root_passwd))
        f.close()
    # 初始化root密码为保存的密码
    with open(root_filename) as file_obj:
        root_passwd = file_obj.read()
    # 初始化缓存
    cache_load()
    print('【初始化完成！】')
    # 载入底层菜单
    boost()


# 登录
def login():
    global passwd_count
    username = 'root'
    print('请登录 >>>>>>>>>')
    while True:
        user = input('登录名：')
        pwd = input('密码：')
        if user == username and pwd == root_passwd:
            print('【登录成功！欢迎登录！】')
            passwd_count = 0
            break
        else:
            passwd_count += 1
            print('【密码错误！登录失败！当前尝试次数为%s次。】' % passwd_count)
            if passwd_count % 3 == 0:
                print('【密码错误次数过多，请等待%s秒后再试！】' % (5 * passwd_count))
                time.sleep(5 * passwd_count)
                return boost()


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
            main_page()
        elif user_numb == '0':
            print("【退出成功！】")
            sys.exit()
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
        print("10-从缓存记录中读取")
        print("0-退出登录")
        print("--—---------------—--")
        user_numb = input("请输入功能序号：")
        user_numb = user_numb
        if user_numb == '1':
            add_info()
        elif user_numb == '2':
            modify_info()
        elif user_numb == '3':
            delete_info()
        elif user_numb == '4':
            query_info()
        elif user_numb == '5':
            query_all_info()
        elif user_numb == '6':
            delete_all_info()
        elif user_numb == '7':
            change_the_root_password()
        elif user_numb == '8':
            save()
        elif user_numb == '9':
            load()
        elif user_numb == '10':
            cache_load()
        elif user_numb == '0':
            print("【已登出！】")
            break
        else:
            print("输入有误，请重新输入！")
            os.system('pause')


# 1-添加学生信息
def add_info():
    global info
    global cache_count
    s_id = input("请输入学号：")
    for i in info:
        if s_id == i["id"]:
            print("【此用户已存在，请勿重复添加】")
            return
    s_name = input("请输入姓名：")
    s_gender = input("请输入性别：")
    s_birthday = input("请输入生日：")

    info_dict = dict()
    info_dict["id"] = s_id
    info_dict["name"] = s_name
    info_dict["gender"] = s_gender
    info_dict["birthday"] = s_birthday

    info.append(info_dict)
    print("【添加成功！】")
    cache_save()
    os.system('pause')


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
            s_gender = input("请重新输入性别：")
            s_birthday = input("请重新输入生日：")

            info_dict = dict()
            info_dict["id"] = s_id
            info_dict["name"] = s_name
            info_dict["gender"] = s_gender
            info_dict["birthday"] = s_birthday

            info.append(info_dict)
            print("【修改成功！】")
            cache_save()
            break
    else:
        print("【该学生不存在！】")

    os.system('pause')


# 3-删除学生信息
def delete_info():
    global info
    del_id = input("请输入您删除的学生学号：")
    for i in info:
        if del_id == i["id"]:
            info.remove(i)
            print("【删除成功！】")
            cache_save()
            break
    else:
        print("【该学生不存在！】")

    os.system('pause')


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

    os.system('pause')


# 5-查询所有学生信息
def query_all_info():
    print(*info, sep='\n')
    print("【已查出所有信息！】")

    os.system('pause')


# 6-删除所有学生信息
def delete_all_info():
    global info
    i_want_delete_all_info = really_do_this(i='删除所有学生信息')
    if i_want_delete_all_info == 'root':
        info = list()
        print("【删除成功！】")
    else:
        do_not_this()

    os.system('pause')


# 7-修改root密码
def change_the_root_password():
    global root_passwd
    print('请输入原密码 >>>>>>>>>')
    pwd = input('原密码：')
    if pwd == root_passwd:
        print('请输入新密码 >>>>>>>>>')
        root_passwd = input('新密码：')
        f = open(root_filename, "w")
        f.write(str(root_passwd))
        f.close()
        return boost()
    else:
        print('【密码错误！】')
        do_not_this()

    os.system('pause')


# 8-保存学生信息到文件（students.npy)
def save():
    i = really_do_this(i='保存学生信息到文件')
    if i == 1:
        if not os.path.exists(student_filename):
            f = open(student_filename, "x")
            f.close()
        numpy.save(student_filename, numpy.array(info))
        print("【存储成功！】")
    else:
        do_not_this()

    os.system('pause')


# 9-从文件中读取数据（students.npy)
def load():
    global info
    i = really_do_this(i='从文件中读取数据')
    if i == 1:
        load_indeed()
    else:
        do_not_this()

    os.system('pause')


# 缓存文件名设置
def cache_filename_set(i):
    global cache_filename
    if i == 0:
        cache_filename = '%s\\cache%s.npy' % (folder1, len(cache_count) - 1)
    else:
        cache_filename = '%s\\cache%s.npy' % (folder1, len(cache_count))


# 存储缓存
def cache_save():
    global cache_count
    global cache_filename
    cache_filename_set(i=1)
    if not os.path.exists(cache_filename):
        f = open(cache_filename, "x")
        f.close()
    numpy.save(cache_filename, numpy.array(info))
    cache_count.append('H')
    numpy.save(cache_count_filename, numpy.array(cache_count))


# 读取缓存
def cache_load():
    global cache_count
    global cache_filename
    global info
    if not os.path.exists(cache_filename):
        print("【还没有缓存数据！】")  # 打开失败，文件不存在说明没有数据保存
    else:
        a = numpy.load(cache_count_filename, allow_pickle=True)
        cache_count = a.tolist()
        cache_filename_set(i=0)
        b = numpy.load(cache_filename, allow_pickle=True)
        info = b.tolist()
        print("【读取全局缓存成功！】")


# 你真的要这么做吗？
def really_do_this(i):
    if input("你真的想要%s吗？输入 root 来确定。\n请输入 root >>>>>>>>>" % i) == 'root':
        return 1
    else:
        return 0


# 我不想这么做
def do_not_this():
    print("【已取消！】")
    return main_page()


# 从文件中读取数据的实现
def load_indeed():
    global info
    if not os.path.exists(student_filename):
        print("【还没有储存数据！】")  # 打开失败，文件不存在说明没有数据保存
    else:
        a = numpy.load(student_filename, allow_pickle=True)
        info = a.tolist()
        print("【读取成功！】")


# main()
global_initialization()
