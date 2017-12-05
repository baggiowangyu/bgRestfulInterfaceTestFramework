# -*- coding: utf-8 -*-


import time


# 本模块用于生成测试结果


class gmReporter:

    # email上报相关参数
    sender_email_address = ""
    sender_email_username = ""
    sender_email_password = ""
    receiver_email_list = ""

    # 测试报告相关变量
    result_file_name = ""
    file_object = ""

    def __init__(self):
        return


    def __del__(self):
        return


    def set_email_info(self):


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
    gmvcs_uom_device.init("执法视音频一体化管理平台统一运维管理平台设备管理模块")

