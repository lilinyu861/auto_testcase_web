import requests


class Test(object):
    def __init__(self, url, header_names, header_values, para_names, para_values):
        self.len1 = len(header_names)
        self.len2 = len(para_names)
        self.url = url

    # 接口测试
    # post 请求
    def test_interface_post(self, url, header_names, header_values, para_names, para_values):
        # 报文头headers
            headers = {header_names[i]: header_values[i] for i in range(self.len1)}
            # headers = {header_name: header_value for header_name in header_names, for header_value in header_values}
        # 报文体body
            data = {para_names[i]: para_values[i] for i in range(self.len2)}
            # data = {para_name: para_value for para_name in para_names, for para_value in para_values}
        # 发送报文，response接受返回报文
            response = requests.post(url, json=data, headers=headers)
        # 返回响应报文response
            return response.text

    # get 请求
    def test_interface_get(self, url, header_names, header_values, para_names, para_values):
        # # 报文头headers
        #     headers = {header_name: header_value for header_name in header_names, for header_value in header_values}
        # # 报文体body
        #     data = {para_name: para_value for para_name in para_names, for para_value in para_values}
        # # 发送报文，response接受返回报文
        #     response = requests.get(url, json=data, headers=headers)
        # # 返回响应报文response
        #     return response.text
        pass

    # patch 请求
    def test_interface_patch(self, url, header_names, header_values, para_names, para_values):
        # # 报文头headers
        # headers = {header_name: header_value for header_name in header_names, for header_value in header_values}
        # # 报文体body
        # data = {para_name: para_value for para_name in para_names, for para_value in para_values}
        # # 发送报文，response接受返回报文
        # response = requests.patch(url, json=data, headers=headers)
        # # 返回响应报文response
        # return response.text
        pass

    # put请求
    def test_interface_put(self, url, header_names, header_values, para_names, para_values):
        # # 报文头headers
        # headers = {header_name: header_value for header_name in header_names, for header_value in header_values}
        # # 报文体body
        # data = {para_name: para_value for para_name in para_names, for para_value in para_values}
        # # 发送报文，response接受返回报文
        # response = requests.put(url, json=data, headers=headers)
        # # 返回响应报文response
        # return response.text
        pass

    # delete请求
    def test_interface_delete(self, url, header_names, header_values, para_names, para_values):
        # # 报文头headers
        # headers = {header_name: header_value for header_name in header_names, for header_value in header_values}
        # # 报文体body
        # data = {para_name: para_value for para_name in para_names, for para_value in para_values}
        # # 发送报文，response接受返回报文
        # response = requests.delete(url, json=data, headers=headers)
        # # 返回响应报文response
        # return response.text
        pass



