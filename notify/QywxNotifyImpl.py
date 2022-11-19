#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/11/19
# QywxNotifyImpl.py
import json

import requests

from notify.BaseNotify import BaseNotify


class QywxNotifyImpl(BaseNotify):
    """
    企业微信通知

    """

    def __init__(self, key: str, mentioned_list: [], mentioned_mobile_list: []):
        self.key = key
        self.mentioned_list = mentioned_list
        self.mentioned_mobile_list = mentioned_mobile_list

    def notify(self, content) -> bool:
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_list": self.mentioned_list,
                "mentioned_mobile_list": self.mentioned_mobile_list
            }
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}"

        r = requests.post(url, data=json.dumps(data)).json()
        return r["errcode"] == 0


if __name__ == '__main__':
    n = QywxNotifyImpl("58a7fecf-ec17-4de7-a794-b93ca80f23c6", [], [])
    print(n.notify("111112222"))
