import time
from tkinter import *
import win32api, win32con

from adspower_controller import AdspowerController
from aolmail_operater import AolMailOperater
from base_ssn_info import SsnInfo
from bluebird_operation import BlueBird
from ks_site_operater import KSGov
from read_excel import ExcelData

adspowercontroller = AdspowerController()

kSGov = None
aolMailOperater = None
blueBird = None
autoNext = False
ssnInfoDatas = None
currentSsn = None


def open_ks_site_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.open_ks_site()


# def create_ksgov_account_event():
#     kSGov.create_ksgov_account()


def fill_create_ksgov_account_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    # ssnInfo = SsnInfo("7", "annalisa", "crain", "1054 linden avenue", "palm harbor", "FL", "34684", "7276231793",
    #                   "262781969", "1983", "2", "28", "c65001083568", "1983-02-28", "", "F", "FL", "",
    #                   "electric avenue", "electric avenue", "11/23/2015", "05/21/2020", "Amberfffca8591", "462D8112",
    #                   "8479", "50a47019", "3959bcfc", "", "10", "0", "", "Cleaning", "Vacuums Floors", "yqld2976",
    #                   "LucianMarshsag@aol.com", None, "")

    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill_create_ksgov_account(currentSsn)
        write_log_to_Text("打开ks网站并填写信息--成功")


def login_ks_site_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.login_ks_site(currentSsn)
        write_log_to_Text("打开ks登录页面填写信息--成功")


def fill1_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill1_ks_all_info(currentSsn, autoNext)
        write_log_to_Text("第1项操作--成功")
    if autoNext:
        fill2_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "2")


def fill2_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill2_ks_all_info(currentSsn, autoNext)
        write_log_to_Text("第2项操作--成功")
    if autoNext:
        fill3_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "3")


def fill3_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill3_ks_all_info(currentSsn, autoNext)
        write_log_to_Text("第3项操作--成功")
    if autoNext:
        fill4_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "4-0")


def fill4_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.fill4_ks_all_info(autoNext)
    write_log_to_Text("第4项操作--成功")
    if autoNext:
        fill4_1_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "4-1")


def fill4_1_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill4_1_ks_all_info(currentSsn, autoNext)
        write_log_to_Text("第4-1项操作--成功")
    if autoNext:
        fill4_2_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "4-2")


def fill4_2_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        kSGov.fill4_2_ks_all_info(currentSsn, autoNext)
        write_log_to_Text("第4-2项操作--成功")
    if autoNext:
        fill4_3_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "4-3")


def fill4_3_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.fill4_3_ks_all_info(autoNext)
    write_log_to_Text("第4-3项操作--成功")
    if autoNext:
        fill5_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "5")


def fill5_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.fill5_ks_all_info(autoNext)
    write_log_to_Text("第5项操作--成功")
    if autoNext:
        fill6_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "6-0")


def fill6_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    routing_number = init_routing_number_Text.get('0.0', 'end').strip()
    bank_account = init_account_number_Text.get('0.0''end').strip()
    if len(routing_number) == 0 or len(bank_account) == 0:
        win32api.MessageBox(0, "请输入银行账号", "提醒", win32con.MB_OK)
    else:
        kSGov.fill6_ks_all_info(autoNext)
        write_log_to_Text("第6项操作--成功")
        if autoNext:
            fill6_1_ks_all_info_event()
            init_current_task_Text.delete(1.0, END)
            init_current_task_Text.insert(1.0, "6-1")


def fill6_1_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.fill6_1_ks_all_info(autoNext)
    write_log_to_Text("第6-1项操作--成功")
    if autoNext:
        fill9_ks_all_info_event()
        init_current_task_Text.delete(1.0, END)
        init_current_task_Text.insert(1.0, "9")


def fill9_ks_all_info_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.fill9_ks_all_info(autoNext)
    write_log_to_Text("第9项操作--成功")


def open_adspower_event():
    if ssnInfoDatas is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        user_id = init_current_adsp_id_Text.get('0.0', 'end').strip()
        if len(user_id) == 0:
            win32api.MessageBox(0, "请正确填写adspower的ID", "提醒", win32con.MB_OK)
        else:
            if adspowercontroller.set_proxy_city(user_id, "US", currentSsn.state, currentSsn.city):
                adspowercontroller.open_adspower(user_id)
                write_log_to_Text("修改adspower城市并打开--成功")
            else:
                win32api.MessageBox(0, "代理设置失败请重试", "提醒", win32con.MB_OK)


def clear_adspower_event():
    global kSGov
    kSGov = KSGov(adspowercontroller.driver)
    kSGov.clear_browser_info()
    write_log_to_Text("清理浏览器--成功")


def open_excel_event():
    global ssnInfoDatas
    global currentSsn
    data_path = "./ks100.xlsx"
    sheetname = "Sheet1"
    get_data = ExcelData(data_path, sheetname)
    ssnInfoDatas = get_data.readExcel()
    currentSsn = SsnInfo(ssnInfoDatas[0]["id"], ssnInfoDatas[0]["first_name"],
                         ssnInfoDatas[0]["last_name"], ssnInfoDatas[0]["address"], ssnInfoDatas[0]["city"],
                         ssnInfoDatas[0]["state"], ssnInfoDatas[0]["zip"], ssnInfoDatas[0]["home_phone"],
                         ssnInfoDatas[0]["ssn"], ssnInfoDatas[0]["birth_year"], ssnInfoDatas[0]["birth_month"],
                         ssnInfoDatas[0]["birth_day"], ssnInfoDatas[0]["drivers_license"], ssnInfoDatas[0]["dob"],
                         ssnInfoDatas[0]["issu_year"], ssnInfoDatas[0]["gender"], ssnInfoDatas[0]["drivers_state"],
                         ssnInfoDatas[0]["is_test"], ssnInfoDatas[0]["employer"], ssnInfoDatas[0]["occupation"],
                         ssnInfoDatas[0]["job_begin_date"], ssnInfoDatas[0]["job_end_date"],
                         ssnInfoDatas[0]["user_name"],
                         ssnInfoDatas[0]["password"], ssnInfoDatas[0]["pin_code"], ssnInfoDatas[0]["secury_question"],
                         ssnInfoDatas[0]["security_code"], ssnInfoDatas[0]["occupation1"], ssnInfoDatas[0]["infotype"],
                         ssnInfoDatas[0]["status"], ssnInfoDatas[0]["ftime"], ssnInfoDatas[0]["intro1"],
                         ssnInfoDatas[0]["intro2"], ssnInfoDatas[0]["email_pass"], ssnInfoDatas[0]["email"],
                         ssnInfoDatas[0]["job_address"], ssnInfoDatas[0]["work_phone"])

    result_data_Text.delete(1.0, END)
    result_data_Text.insert(1.0, "当前数据城市：" + str(currentSsn.city))
    result_data_Text.insert(1.0, "当前数据编号：" + str(currentSsn.id) + "\n")
    write_log_to_Text("excel打开--成功")


def select_excel_id_event():
    if ssnInfoDatas is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        try:
            global currentSsn
            excel_index = int(init_current_id_Text.get('0.0', 'end').strip()) - 1
            currentSsn = SsnInfo(ssnInfoDatas[excel_index]["id"], ssnInfoDatas[excel_index]["first_name"],
                                 ssnInfoDatas[excel_index]["last_name"], ssnInfoDatas[excel_index]["address"],
                                 ssnInfoDatas[excel_index]["city"],
                                 ssnInfoDatas[excel_index]["state"], ssnInfoDatas[excel_index]["zip"],
                                 ssnInfoDatas[excel_index]["home_phone"],
                                 ssnInfoDatas[excel_index]["ssn"], ssnInfoDatas[excel_index]["birth_year"],
                                 ssnInfoDatas[excel_index]["birth_month"],
                                 ssnInfoDatas[excel_index]["birth_day"], ssnInfoDatas[excel_index]["drivers_license"],
                                 ssnInfoDatas[excel_index]["dob"],
                                 ssnInfoDatas[excel_index]["issu_year"], ssnInfoDatas[excel_index]["gender"],
                                 ssnInfoDatas[excel_index]["drivers_state"],
                                 ssnInfoDatas[excel_index]["is_test"], ssnInfoDatas[excel_index]["employer"],
                                 ssnInfoDatas[excel_index]["occupation"],
                                 ssnInfoDatas[excel_index]["job_begin_date"], ssnInfoDatas[excel_index]["job_end_date"],
                                 ssnInfoDatas[excel_index]["user_name"],
                                 ssnInfoDatas[excel_index]["password"], ssnInfoDatas[excel_index]["pin_code"],
                                 ssnInfoDatas[excel_index]["secury_question"],
                                 ssnInfoDatas[excel_index]["security_code"], ssnInfoDatas[excel_index]["occupation1"],
                                 ssnInfoDatas[excel_index]["infotype"],
                                 ssnInfoDatas[excel_index]["status"], ssnInfoDatas[excel_index]["ftime"],
                                 ssnInfoDatas[excel_index]["intro1"],
                                 ssnInfoDatas[excel_index]["intro2"], ssnInfoDatas[excel_index]["email_pass"],
                                 ssnInfoDatas[excel_index]["email"],
                                 ssnInfoDatas[excel_index]["job_address"], ssnInfoDatas[excel_index]["work_phone"])
            result_data_Text.delete(1.0, END)
            result_data_Text.insert(1.0, "当前数据城市：" + str(currentSsn.city))
            result_data_Text.insert(1.0, "当前数据编号：" + str(currentSsn.id) + "\n")
            write_log_to_Text("选取ID信息--成功")
        except Exception as er:
            win32api.MessageBox(0, er, "请输入正确的ID", win32con.MB_OK)


def select_next_excel_id_event():
    if ssnInfoDatas is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        try:
            global currentSsn
            excel_index = int(init_current_id_Text.get('0.0', 'end').strip())
            currentSsn = SsnInfo(ssnInfoDatas[excel_index]["id"], ssnInfoDatas[excel_index]["first_name"],
                                 ssnInfoDatas[excel_index]["last_name"], ssnInfoDatas[excel_index]["address"],
                                 ssnInfoDatas[excel_index]["city"],
                                 ssnInfoDatas[excel_index]["state"], ssnInfoDatas[excel_index]["zip"],
                                 ssnInfoDatas[excel_index]["home_phone"],
                                 ssnInfoDatas[excel_index]["ssn"], ssnInfoDatas[excel_index]["birth_year"],
                                 ssnInfoDatas[excel_index]["birth_month"],
                                 ssnInfoDatas[excel_index]["birth_day"], ssnInfoDatas[excel_index]["drivers_license"],
                                 ssnInfoDatas[excel_index]["dob"],
                                 ssnInfoDatas[excel_index]["issu_year"], ssnInfoDatas[excel_index]["gender"],
                                 ssnInfoDatas[excel_index]["drivers_state"],
                                 ssnInfoDatas[excel_index]["is_test"], ssnInfoDatas[excel_index]["employer"],
                                 ssnInfoDatas[excel_index]["occupation"],
                                 ssnInfoDatas[excel_index]["job_begin_date"], ssnInfoDatas[excel_index]["job_end_date"],
                                 ssnInfoDatas[excel_index]["user_name"],
                                 ssnInfoDatas[excel_index]["password"], ssnInfoDatas[excel_index]["pin_code"],
                                 ssnInfoDatas[excel_index]["secury_question"],
                                 ssnInfoDatas[excel_index]["security_code"], ssnInfoDatas[excel_index]["occupation1"],
                                 ssnInfoDatas[excel_index]["infotype"],
                                 ssnInfoDatas[excel_index]["status"], ssnInfoDatas[excel_index]["ftime"],
                                 ssnInfoDatas[excel_index]["intro1"],
                                 ssnInfoDatas[excel_index]["intro2"], ssnInfoDatas[excel_index]["email_pass"],
                                 ssnInfoDatas[excel_index]["email"],
                                 ssnInfoDatas[excel_index]["job_address"], ssnInfoDatas[excel_index]["work_phone"])
            init_current_id_Text.delete(1.0, END)
            init_current_id_Text.insert(1.0, int(excel_index) + 1)
            result_data_Text.delete(1.0, END)
            result_data_Text.insert(1.0, "当前数据城市：" + str(currentSsn.city))
            result_data_Text.insert(1.0, "当前数据编号：" + str(currentSsn.id) + "\n")
            write_log_to_Text("数据进行下一个--成功")
        except Exception as er:
            win32api.MessageBox(0, er, "请输入正确的ID", win32con.MB_OK)


def open_gmail_event():
    global aolMailOperater
    aolMailOperater = AolMailOperater(adspowercontroller.driver)
    aolMailOperater.open_aol_mail_site()


def login_gmail_event():
    aolMailOperater.login_aol_mail("LacyHaydeniyj@aol.com")


def fill_aol_mail_password_event():
    aolMailOperater.fill_aol_mail_password("pvol6148")


def open_bluebird_site_event():
    global blueBird
    blueBird = BlueBird(adspowercontroller.driver)
    blueBird.open_bluebird_site()


def crate_bluebird_account_event():
    if currentSsn is None:
        win32api.MessageBox(0, "请先读取Excel", "提醒", win32con.MB_OK)
    else:
        blueBird.crate_bluebird_account(currentSsn)


def write_log(log_info):
    filename = 'log.txt'
    with open(filename, 'a') as file_object:
        file_object.write(log_info + "\n")


def ks_create_success_event():
    write_log("ID:" + str(currentSsn.id) + "创建账号成功")
    write_log_to_Text("ID:" + str(currentSsn.id) + "创建账号成功")


def ks_fill_success_event():
    write_log("ID:" + str(currentSsn.id) + "填写信息成功")
    write_log_to_Text("ID:" + str(currentSsn.id) + "填写信息成功")


# 获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


# 日志动态打印
def write_log_to_Text(logmsg):
    global LOG_LINE_NUM
    current_time = get_current_time()
    logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
    # if LOG_LINE_NUM <= 45:
    log_data_Text.insert(END, logmsg_in)
    LOG_LINE_NUM = LOG_LINE_NUM + 1
    # else:
    #     log_data_Text.delete(1.0, 2.0)
    #     log_data_Text.insert(END, logmsg_in)


LOG_LINE_NUM = 0


def get_auto_next_event():
    global autoNext
    if CheckVar1.get() == "1":
        autoNext = True
    else:
        autoNext = False


init_window = Tk()  # 实例化出一个父窗口

init_window.title("USA SSN Info   by: spider")  # 窗口名
# self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
init_window.geometry('1068x681+10+10')
# self.init_window_name["bg"] = "pink" #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
# self.init_window_name.attributes("-alpha", # 0.9)                          #虚化，值越小虚化程度越高 标签
init_data_label = Label(init_window, text="KS网站操作")
init_data_label.grid(row=0, column=0)
result_data_label = Label(init_window, text="日志")
result_data_label.grid(row=0, column=12)
log_label = Label(init_window, text="基本信息")
log_label.grid(row=12, column=0)
# 文本框

init_data_Text = Canvas(init_window, width=560, height=480, bg='pink')  # 原始数据录入框
init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
log_data_Text = Text(init_window, width=70, height=49)  # 处理结果展示
log_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
result_data_Text = Text(init_window, width=66, height=9)  # 日志框
result_data_Text.grid(row=13, column=0, columnspan=10)

# 按钮
# self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,
#                                       )  # 调用内部方法  加()为直接调用
# self.str_trans_to_md5_button.grid(row=1, column=11)

init_current_adsp_id_label = Label(init_window, text="当前浏览器ID:")
init_current_adsp_id_label.grid(row=0, column=2)

init_current_adsp_id_Text = Text(init_window, width=10, height=1, bg='red')  # 原始数据录入框
init_current_adsp_id_Text.grid(row=0, column=3)
init_current_adsp_id_Text.insert(0.0, "i6wnod")

clear_adspower_event = Button(init_window, text="清理缓存", bg="lightblue", width=20,
                              command=clear_adspower_event)  # 调用内部方法  加()为直接调用
clear_adspower_event.grid(row=0, column=1)

open_adspower_event = Button(init_window, text="打开adspower浏览器", bg="lightblue", width=20,
                             command=open_adspower_event)  # 调用内部方法  加()为直接调用
open_adspower_event.grid(row=0, column=12)

open_adspower_event = Button(init_window, text="打开excel", bg="lightblue", width=20,
                             command=open_excel_event)  # 调用内部方法  加()为直接调用
open_adspower_event.grid(row=0, column=13)

open_ks_site_event = Button(init_window, text="打开KS注册页面", bg="lightblue", width=15,
                            command=open_ks_site_event)  # 调用内部方法  加()为直接调用
open_ks_site_event.grid(row=1, column=0)

fill_create_ksgov_account_event = Button(init_window, text="填写创建KS信息", bg="lightblue", width=15,
                                         command=fill_create_ksgov_account_event)  # 调用内部方法  加()为直接调用
fill_create_ksgov_account_event.grid(row=1, column=1)

login_ks_site_event = Button(init_window, text="ks打开登录页面并填写", bg="lightblue", width=15,
                             command=login_ks_site_event)  # 调用内部方法  加()为直接调用
login_ks_site_event.grid(row=2, column=0)

fill1_ks_all_info_event = Button(init_window, text="ks填写基本信息1", bg="lightblue", width=15,
                                 command=fill1_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill1_ks_all_info_event.grid(row=2, column=1)

fill2_ks_all_info_event = Button(init_window, text="ks填写基本信息2", bg="lightblue", width=15,
                                 command=fill2_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill2_ks_all_info_event.grid(row=3, column=0)

fill3_ks_all_info_event = Button(init_window, text="ks填写基本信息3", bg="lightblue", width=15,
                                 command=fill3_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill3_ks_all_info_event.grid(row=3, column=1)

fill4_ks_all_info_event = Button(init_window, text="ks填写基本信息4-0", bg="lightblue", width=15,
                                 command=fill4_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill4_ks_all_info_event.grid(row=4, column=0)

fill4_1_ks_all_info_event = Button(init_window, text="ks填写基本信息4-1", bg="lightblue", width=15,
                                   command=fill4_1_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill4_1_ks_all_info_event.grid(row=4, column=1)

fill4_2_ks_all_info_event = Button(init_window, text="ks填写基本信息4-2", bg="lightblue", width=15,
                                   command=fill4_2_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill4_2_ks_all_info_event.grid(row=5, column=0)

fill4_3_ks_all_info_event = Button(init_window, text="ks填写基本信息4-3", bg="lightblue", width=15,
                                   command=fill4_3_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill4_3_ks_all_info_event.grid(row=5, column=1)

fill5_ks_all_info_event = Button(init_window, text="ks填写基本信息5", bg="lightblue", width=15,
                                 command=fill5_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill5_ks_all_info_event.grid(row=6, column=0)

fill6_ks_all_info_event = Button(init_window, text="ks填写基本信息6", bg="lightblue", width=15,
                                 command=fill6_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill6_ks_all_info_event.grid(row=6, column=1)

fill6_1_ks_all_info_event = Button(init_window, text="ks填写基本信息6-1", bg="lightblue", width=15,
                                   command=fill6_1_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill6_1_ks_all_info_event.grid(row=7, column=0)

fill9_ks_all_info_event = Button(init_window, text="ks填写基本信息9", bg="lightblue", width=15,
                                 command=fill9_ks_all_info_event)  # 调用内部方法  加()为直接调用
fill9_ks_all_info_event.grid(row=7, column=1)

CheckVar1 = IntVar()
CheckVar1.set("0")
init_check_auto_next = Checkbutton(init_window, text="是否自动下一步", variable=CheckVar1,
                                   onvalue="1", offvalue="0", height=1, width=15,
                                   command=get_auto_next_event)
init_check_auto_next.grid(row=8, column=0)

init_current_id_label = Label(init_window, text="当前excel_ID:")
init_current_id_label.grid(row=1, column=2)

init_current_id_Text = Text(init_window, width=10, height=1, bg='red')  # 当前excel——id
init_current_id_Text.insert(1.0, "1")
init_current_id_Text.grid(row=1, column=3)

select_excel_id_event = Button(init_window, text="选取", bg="lightblue", width=5,
                               command=select_excel_id_event)  # 调用内部方法  加()为直接调用
select_excel_id_event.grid(row=2, column=2)

select_next_excel_id_event = Button(init_window, text="下一条", bg="lightblue", width=5,
                                    command=select_next_excel_id_event)  # 调用内部方法  加()为直接调用
select_next_excel_id_event.grid(row=2, column=3)

init_current_task_label = Label(init_window, text="当前任务ID:")
init_current_task_label.grid(row=3, column=2)

init_current_task_Text = Text(init_window, width=10, height=1, bg='red')  # 当前任务ID
init_current_task_Text.insert(1.0, "1")
init_current_task_Text.grid(row=3, column=3)

ks_create_success_event = Button(init_window, text="KS创建成功", bg="lightblue", width=15,
                                 command=ks_create_success_event)  # 调用内部方法  加()为直接调用
ks_create_success_event.grid(row=4, column=2)

ks_fill_success_event = Button(init_window, text="KS填写成功", bg="lightblue", width=15,
                               command=ks_fill_success_event)  # 调用内部方法  加()为直接调用
ks_fill_success_event.grid(row=4, column=3)

init_routing_number_label = Label(init_window, text="Routing Number:")
init_routing_number_label.grid(row=9, column=0)

init_routing_number_Text = Text(init_window, width=15, height=1, bg='red')  # 银行routing
init_routing_number_Text.grid(row=9, column=1)

init_account_number_label = Label(init_window, text="Account Number:")
init_account_number_label.grid(row=9, column=2)

init_account_number_Text = Text(init_window, width=15, height=1, bg='red')  # 银行账号
init_account_number_Text.grid(row=9, column=3)

open_bluebird_site_event = Button(init_window, text="打开bluebird网站", bg="lightblue", width=15,
                                  command=open_bluebird_site_event)  # 调用内部方法  加()为直接调用
open_bluebird_site_event.grid(row=6, column=2)

crate_bluebird_account_event = Button(init_window, text="填写bluebird信息", bg="lightblue", width=15,
                                      command=crate_bluebird_account_event)  # 调用内部方法  加()为直接调用
crate_bluebird_account_event.grid(row=6, column=3)

init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
# # 功能函数
# def str_trans_to_md5(self):
#     src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
#     # print("src =",src)
#     if src:
#         try:
#             myMd5 = hashlib.md5()
#             myMd5.update(src)
#             myMd5_Digest = myMd5.hexdigest()
#             # print(myMd5_Digest)
#             # 输出到界面
#             self.result_data_Text.delete(1.0, END)
#             self.result_data_Text.insert(1.0, myMd5_Digest)
#             self.write_log_to_Text("INFO:str_trans_to_md5 success")
#         except:
#             self.result_data_Text.delete(1.0, END)
#             self.result_data_Text.insert(1.0, "字符串转MD5失败")
#     else:
#         self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
