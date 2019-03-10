import scrapy

""" scrapy.Spider 子类定义了一些属性和方法
name: 用来标识一个爬虫
start_requests: 返回包含 request 对象的迭代器，scrapy 调度这些请求，返回 response 对象
parse: 处理返回的 response 对象
"""
class testSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        cookies = {"User":"1616202", "LogonType":"%E7%8F%AD%E7%BA%A7", "ASP.NET_SessionId":"r3h45gppenfumljbvvu42l1s", "DedHasLogin":"1", "ASPSESSIONIDQASSDDBA":"NMBABFIAEIAOPGBPONFEAGEN", "UserLanguage":"zh-CN", "CanViewPhotoFilter":"161620218"}
        #vcode_url = "http://ded.nuaa.edu.cn/NetEAn/User/GetCode.asp"
        #login_url = "http://ded.nuaa.edu.cn/NetEAn/User/login.asp"
        crawl_url = 'http://ded.nuaa.edu.cn/netean/newpage/xsyh/default.asp'
        
        #yield scrapy.Request(url=login_url, callback=self.login)
        yield scrapy.Request(url=crawl_url, cookies=cookies, callback=self.parse)

    def login(self, response):
        pass         

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #response.body
        print(response.body)
