# -*- coding: utf-8 -*-


import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# 本模块用于生成测试结果


class gmReporter:

    # email上报相关参数
    smtp_object = ""
    reporter_url = ""
    recievcers_url = ""
    smtp_username = ""
    smtp_password = ""
    smtp_server_url = ""

    # 测试报告相关变量
    result_file_name = ""
    file_object = ""

    def __init__(self, reporter, recievcers, smtp_id, smtp_pwd, smtp_server):
        self.reporter_url = reporter
        self.recievcers_url = recievcers
        self.smtp_username = smtp_id
        self.smtp_password = smtp_pwd
        self.smtp_server_url = smtp_server
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
        self.file_object = open(self.result_file_name.decode('utf-8').encode('gbk'), "w")

        # 写入报告标头
        report_context = test_name + "自动化测试报告"
        self.file_object.writelines(report_context)
        self.file_object.writelines("\r\n")

        report_context = "测试开始时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\r\n"
        self.file_object.writelines(report_context)
        self.file_object.writelines("\r\n")

        report_context = "-------------------------------------------------"
        self.file_object.writelines(report_context)
        self.file_object.writelines("\r\n")


    def close(self):
        self.file_object.close()

        # 发送邮件
        self.login_report_email_server(self.smtp_server_url, self.smtp_username, self.smtp_password)
        self.send_report_email(self.smtp_username,
                               self.recievcers_url,
                               "测试报告".decode('utf-8').encode('gbk'),
                               "这是来自一个自动化测试工具的测试报告自动发布模块发送的邮件".decode('utf-8').encode('gbk'),
                               self.result_file_name.decode('utf-8').encode('gbk'))


    def write_testcase_result(self, testcase_name, testcase_result, testcase_consume_time):
        # 参数表说明：
        # testcase_name：测试用例名称
        # testcase_result：测试用例结果
        # testcase_consume_time：测试用例消耗时间
        self.file_object.writelines(testcase_name)
        self.file_object.writelines("\r\n")
        self.file_object.writelines(testcase_result)
        self.file_object.writelines("\r\n")
        self.file_object.writelines(testcase_consume_time)
        self.file_object.writelines("\r\n")
        self.file_object.writelines("\r\n")


if __name__ == '__main__':
    reporter = "lrhw_crashrpt@sina.com"
    recievcer = ['weiyonggao@gosuncn.com', 'wangyu@gosuncn.com', '52864380@qq.com']
    smtp_user = "lrhw_crashrpt@sina.com"
    smtp_pass = "871511"
    smtp_url = "smtp.sina.com"

    gmvcs_uom_device = gmReporter(reporter, recievcer, smtp_user, smtp_pass, smtp_url)
    gmvcs_uom_device.init("执法视音频一体化管理平台统一运维管理平台设备管理模块")
    gmvcs_uom_device.write_testcase_result("测试用例名称1", "测试用例测试结果1", "测试用例执行消耗时间1")
    gmvcs_uom_device.write_testcase_result("测试用例名称2", "测试用例测试结果2", "测试用例执行消耗时间2")
    gmvcs_uom_device.write_testcase_result("测试用例名称3", "测试用例测试结果3", "测试用例执行消耗时间3")
    gmvcs_uom_device.write_testcase_result("测试用例名称4", "测试用例测试结果4", "测试用例执行消耗时间4")
    gmvcs_uom_device.close()



