# -*- coding: utf-8 -*-


import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


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
        code, msg = self.smtp_object.connect(email_host, 25)
        print "connect smtp server ..." + str(code)
        print "connect smtp server ..." + msg
        code, resp = self.smtp_object.login(email_username, email_password)
        print "login smtp server ..." + str(code)
        print "login smtp server ..." + resp


    def send_report_email(self, sender, recievers, title, message_text, filepath):

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = title
        msgRoot['From'] = sender

        # 增加正文
        content = MIMEText(message_text, 'plain')
        msgRoot.attach(content)

        # 构造附件
        att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="测试报告.txt"'
        msgRoot.attach(att)

        #try:
        senderrs = self.smtp_object.sendmail(sender, recievers, msgRoot.as_string())
        print senderrs
        #except smtplib.SMTPException:
        #    print "发送邮件失败！"


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

    gmvcs_uom_device.login_report_email_server("smtp.sina.com", "lrhw_crashrpt@sina.com", "871511")
    gmvcs_uom_device.send_report_email("lrhw_crashrpt@sina.com",
                                       ['wangyu@gosuncn.com', '52864380@qq.com'],
                                       "测试报告",
                                       "这是来自一个自动化测试工具的测试报告自动发布模块发送的邮件",
                                       "D:\\test.txt")

