# -*- coding: utf-8 -*-


import sys
sys.path.append("..")
import Interface.gmInterface
import Report.gmTestReport
import Base.gmBase
import time


reporter = "lrhw_crashrpt@sina.com"
recievcer = ['weiyonggao@gosuncn.com', 'wangyu@gosuncn.com', '52864380@qq.com']
smtp_user = "lrhw_crashrpt@sina.com"
smtp_pass = "871511"
smtp_url = "smtp.sina.com"


if __name__ == '__main__':
    # 一个模块的测试用例创建一个 TestCase.py
    # 本文件用于测试执法视音频一体化管理平台.统一运维平台.采集站设备管理模块接口
    #
    module_server_base_url = "http://10.10.9.102:6222/gmvcs/uom/device"
    gmvcs_uom_device = Interface.gmInterface()
    gmvcs_uom_device.init(module_server_base_url)


    testcase_name = "查询所有工作站"
    testcase_detail = "查询条件为：..."
    start_time = time.time()
    result_json = gmvcs_uom_device.call_interface(interface="/workstation/org/all", method="GET")
    end_time = time.time()

    finally_result = gmvcs_uom_device.query_result_handle_style1(result_json=result_json)
    Base.gmBase.print_chinese(finally_result)
    Base.gmBase.print_chinese("接口调用耗时：" + str((end_time - start_time) * 1000) + " ms")