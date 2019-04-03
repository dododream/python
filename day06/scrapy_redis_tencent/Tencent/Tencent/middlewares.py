#coding:utf-8

import requests
import random

from .settings import USER_AGENT_LIST as ua_list

class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(ua_list)

        spider.logger.info(request.headers)

        # 在中间件里不要return 一个正常的request
        #return request


class ProxyMiddleware(object):
    def __init__(self):
        self.proxy_api = "http://kps.kdlapi.com/api/getkps/?orderid=975140257435034&num=1&pt=1&sep=1"

        self.proxy = "http://maozhaojun:ntkn0npx@" + requests.get(self.proxy_api).text
        #self.proxy = "http://maozhaojun:ntkn0npx@" + requests.get(proxy_api).json()

        self.count = 0


    def process_request(self, request, spider):

        if self.count <= 10:
            request.meta['proxy'] = self.proxy
            self.count += 1
            spider.logger.info("===" * 10)
            spider.logger.info(self.count)
        else:
            self.proxy = "http://maozhaojun:ntkn0npx@" + requests.get(self.proxy_api).text
            self.count = 0
            request.meta['proxy'] = self.proxy



        #requests.get(proxies={"http:" : "http://user:password@ip:port"})
        # meta 是一个字典，prxoy键对应的值是一个 字符串（相当于我们之前使用的代理的值）
        # 免费代理
        # proxy = "http:/172.81.250.76:16816"
        # 验证代理
        # proxy = "http://maozhaojun:ntkn0npx@172.81.250.76:16816"

        # request.meta['proxy'] = proxy


