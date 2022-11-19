#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gcdd1993 on 2022/11/19
# Launcher.py

from SSLCheck import SSLCheck
from notify.QywxNotifyImpl import QywxNotifyImpl
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

if __name__ == '__main__':
    with open("config.sample.yaml", "r") as f:
        conf = load(f, Loader=Loader)
        print(f"读取配置文件 {conf}")
        # 创建SSLCheck实例
        ssl_checker_list = []
        for domain in conf["domains"]:
            ssl_checker_list.append(SSLCheck(domain))
        # 开始遍历检测SSL证书，并构造通知消息
        msg = ""
        for ssl_checker in ssl_checker_list:
            expire_in_days = ssl_checker.get_ssl_time()
            msg += f"域名 {ssl_checker.domain} 还有 {expire_in_days} 天到期\n"
        # 创建notify实例
        notify_list = []
        for n in conf["notify"]:
            if n["type"] == "QYWX":
                mentioned_list = []
                mentioned_mobile_list = []
                if "mentioned" in n:
                    mentioned_list = n["mentioned"]["name"]
                    mentioned_mobile_list = n["mentioned"]["phone"]
                notify_list.append(QywxNotifyImpl(n["key"], mentioned_list, mentioned_mobile_list))
        for notify in notify_list:
            notify.notify(msg)
