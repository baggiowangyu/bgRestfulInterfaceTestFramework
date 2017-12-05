# -*- coding: utf-8 -*-

import sys
import os
import urllib
import urllib2
import json
import time
import datetime
sys.path.append("..")
import Base.gmBase


#######################################################################################################################
#
# 国迈Restful接口测试类
# 类说明：本类型实现了后台测试服务的接入与调用，以及通用的结果处理
#
#######################################################################################################################

class gmInterface:


    http_url_base = ""


    def __init__(self):
        return


    def __del__(self):
        return


    def init(self, interface_root):
        # 函数说明
        self.http_url_base = interface_root


    def call_interface(self, interface, method, post_data = ""):
        # 函数说明：
        # 根据参数调用Restful接口，得到调用结果

        # 组装接口URL
        request_url = self.http_url_base + interface

        # 分发请求
        try:
            if method == "GET":
                request = urllib2.Request(request_url)
            elif method == "POST":
                # post_data_urlencode = urllib.urlencode(post_data)
                post_data_urlencode = post_data
                request = urllib2.Request(url=request_url, data=post_data_urlencode,
                                          headers={"Content-Type": "application/json"})

            # 读取接口调用结果
            responst_data = urllib2.urlopen(request)
            res = responst_data.read()
        except BaseException:
            res = ""



        return res

    def query_result_handle_style1(self, result_json, expected_count = -1, expected_data = ""):
        # 函数说明：
        # 传入参数为接口调用后返回的json结果字符串、预期的查询结果数目、预期的查询结果数据
        # 当查询结果为0，并且查询的结果与预期结果一致，说明测试通过，否则测试失败
        result = json.loads(result_json)

        if result["code"] == 0:
            if expected_count > 0:
                if len(result["wss"]) == expected_count:
                    #if len(expected_data) > 0:
                    #    # 进到这里说明期望进行结果比对
                    result_string = "结果与预期相匹配"
                else:
                    result_string = "结果数量与预期不匹配"
            else:
                result_string = "结果与预期相匹配"
        elif result["code"] == 1500:
            result_string = "接口返回\"失败\""
        elif result["code"] == 1025:
            result_string = "部门不存在"
        else:
            result_string = "接口返回定义之外的结果"

        return result_string



#######################################################################################################################
#
# 国迈Restful接口测试类，使用范例
#
#######################################################################################################################

if __name__ == '__main__':
    gmvcs_uom_device = gmInterface()
    gmvcs_uom_device.init("http://10.10.9.102:6222/gmvcs/uom/device")

    start_time = time.time()
    result_json = gmvcs_uom_device.call_interface(interface = "/workstation/org/all", method = "GET")
    end_time = time.time()

    finally_result = gmvcs_uom_device.query_result_handle_style1(result_json = result_json)
    Base.gmBase.print_chinese(finally_result)
    Base.gmBase.print_chinese("接口调用耗时：" + str((end_time - start_time) * 1000) + " ms")

