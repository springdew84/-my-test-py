# -*- coding: utf-8 -*-
import base64
import json


class Config:
    index = 0
    random = False
    global_s = False
    enabled = True
    shareOverLan = False
    isDefault = False
    localPort = 1080
    pacUrl = ''
    useOnlinePac = False
    reconnectTimes = 3
    randomAlgorithm = 0
    TTL = 0
    proxyEnable = False
    proxyType = 0
    proxyHost = ''
    proxyPort = 0
    proxyAuthUser = ''
    proxyAuthPass = ''
    authUser = ''
    authPass = ''
    autoban = False
    configs = []

    def __init__(self):
        self.index = 0
        self.random = False
        self.global_s = False
        self.enabled = True
        self.shareOverLan = False
        self.isDefault = False
        self.localPort = 1080
        self.pacUrl = ''
        self.useOnlinePac = False
        self.reconnectTimes = 3
        self.randomAlgorithm = 0
        self.TTL = 0
        self.proxyEnable = False
        self.proxyType = 0
        self.proxyHost = ''
        self.proxyPort = 0
        self.proxyAuthUser = ''
        self.proxyAuthPass = ''
        self.authUser = ''
        self.authPass = ''
        self.autoban = False
        self.configs = []


class ServerInfo:
    # 服务器IP地址 ：服务器端口号 ：协议：加密 ：混淆 ：密码
    server = ''
    server_port = 0
    protocol = 'origin'
    method = 'rc4'
    obfs = 'plain'
    password = ''
    enable = True
    remarks = ''
    remarks_base64 = ''

    def __init__(self, server, server_port, protocol, method, obfs, password):
        self.server = server
        self.server_port = int(server_port)
        self.protocol = protocol
        self.method = method
        self.obfs = obfs
        self.password = password
        self.remarks = server
        self.enable = True

    def __setattr__(self, key, value):
        self.__dict__[key] = value


serverArray = []
config = Config()

if __name__ == '__main__':
    filePath = "r01.txt"
    file1 = open(filePath, "r")
    i = 0
    for row in file1:
        decodeStr = row.replace("ssr://", "").replace("ss://", "")

        decodeStr = decodeStr.replace("_", "+").replace("_", "/")

        # 可选altchars必须是长度为2的对象或ASCII字符串之类的字节它指定使用的替代字母表，而不是“+”和“/”字符。
        # 原因分析:传入的参数的长度不是2的对象，在参数最后加上等于号"="(一个或者两个)
        decodeStr = decodeStr + "=="
        # print(str(i) + "密文：" + decodeStr)

        originStr = base64.b64decode(decodeStr).decode("UTF-8")
        # originStr = base64.urlsafe_b64decode(decodeStr).decode('utf-8')
        # print("解密：" + originStr)

        hostInfoArray = []
        if originStr.find("/?") >= 0:
            hostInfoArray = originStr.split("/?")
        elif originStr.find("/>") >= 0:
            hostInfoArray = originStr.split("/>")
        else:
            raise Exception(print('unkonwn spliter!!!'))

        print(i)
        # print(hostInfoArray[0])

        hostInfo = hostInfoArray[0].split(":")

        # pwdOrigin = hostInfo[5] + '=='
        pwdOrigin = hostInfo[5]

        pwdOrigin = pwdOrigin.replace("_", "+").replace("_", "/")

        print("pwd origin:  " + pwdOrigin)
        pwd = base64.b64decode(pwdOrigin).decode("UTF-8")
        print("pwd:   " + pwd)
        serverInfo = ServerInfo(hostInfo[0], hostInfo[1], hostInfo[2], hostInfo[3], hostInfo[4], pwd)
        serverArray.append(serverInfo)

        i = i + 1

    config.__setattr__('configs', serverArray)
    json_str = json.dumps(config, default=lambda o: o.__dict__, sort_keys=False, indent=4)
    json_str = json_str.replace("global_s", "global")
    print(json_str)

    config_file = open("conf.json", "w")
    config_file.write(json_str)
    config_file.close()

