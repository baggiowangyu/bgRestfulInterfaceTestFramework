# -*- coding: utf-8 -*-


import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 本模块用于生成测试结果


class gmReporter:

    # email上报相关参数
    #email_host = ""
    sender_email_address = ""
    #sender_email_username = ""
    #sender_email_password = ""
    receiver_email_list = ""
    email_content = ""

    smtp_object = ""

    # 测试报告相关变量
    result_file_name = ""
    file_object = ""

    def __init__(self):
        return


    def __del__(self):
        return


    def login_report_email_server(self, email_host, email_username, email_password):
        self.smtp_object = smtplib.SMTP()
        self.smtp_object.connect(email_host, 25)
        self.smtp_object.login(email_username, email_password)


    def send_report_email(self, sender, recievers, message_text, filepath):

        message = MIMEMultipart()
        message['From'] = Header("自动化测试报告", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        # 主题名称
        subject = "XXX 自动化测试报告"
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文
        message.attach(MIMEText(message_text, 'plain', 'utf-8'))

        # 构造附件
        attribute_1 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        attribute_1["Content-Type"] = 'application/octet-stream'
        attribute_1["Content-Disposition"] = 'attachment; filename="测试报告.txt"'
        message.attach(attribute_1)

        try:
            self.smtp_object.sendmail(sender, recievers, message.as_string())
        except smtplib.SMTPException:
            print "发送邮件失败！"


    def init(self, test_name):
        # 先拼接输出报告的路径，打开文件
        self.result_file_name = test_name + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".txt"
        self.file_object = open(self.result_file_name, "w")

        # 写入报告标头
        report_context = test_name + "自动化测试报告"
        self.file_object.writelines(report_context)

        report_context = "测试开始时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.file_object.writelines(report_context)

        report_context = "-------------------------------------------------"
        self.file_object.writelines(report_context)


    def close(self):
        self.file_object.close()

        # 发送邮件


    def write_testcase_result(self, testcase_name, testcase_result, testcase_consume_time):
        # 参数表说明：
        # testcase_name：测试用例名称
        # testcase_result：测试用例结果
        # testcase_consume_time：测试用例消耗时间
        self.file_object.writelines(testcase_name)
        self.file_object.writelines(testcase_result)
        self.file_object.writelines(testcase_consume_time)


if __name__ == '__main__':
    gmvcs_uom_device = gmReporter()
    #gmvcs_uom_device.init("执法视音频一体化管理平台统一运维管理平台设备管理模块")

    gmvcs_uom_device.login_report_email_server("smtp.sina.com", "lrhw_crashrpt", "871511")
    gmvcs_uom_device.send_report_email("lrhw_crashrpt@sina.com",
                                       ["lrhw_crashrpt@sina.com", "wangyu@gosuncn.com"],
                                       "这是来自一个自动化测试工具的测试报告自动发布模块发送的邮件",
                                       "G:\\OpenSource_Extend\\bgPython\\RestfulTestCase.py")

