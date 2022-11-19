#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/11/19
# SSLCheck.py

from datetime import datetime

from urllib3.contrib import pyopenssl


class SSLCheck:
    """
    监控某个域名SSL过期时间

    """

    def __init__(self, domain):
        self.domain = domain

    def get_str_time(self):
        """
        获取SSL证书到期时间，时间格式：20221119200000

        :return:
        """
        x509 = pyopenssl.OpenSSL.crypto.load_certificate(pyopenssl.OpenSSL.crypto.FILETYPE_PEM,
                                                         pyopenssl.ssl.get_server_certificate((self.domain, 443)))
        return x509.get_notAfter().decode()[0:-1]

    def get_ssl_time(self):
        """
        获取SSL证书剩余天数

        :return:
        """
        ssl_time = datetime.strptime(self.get_str_time(), '%Y%m%d%H%M%S')
        return (ssl_time - datetime.now()).days
