项目地址 https://github.com/dataabc/weiboSpider



#### 0x01 微博爬虫 weiboSpider

这是一个代码量极其少的小项目，分析一下功能：

> 1. 输入微博的用户id，爬取对应的各种信息，如微博昵称，粉丝数，发表的微博数和微博内容等
>
> 2. 写入文件



在唯一的一个项目文件的开始，导入了需要用到的一些库，大致可以看到用来进行网络交互的 requests 和用来解析网页结构的 etree，至于 traceback，简单查了一下，traceback 库用于异常处理，项目中用 traceback.print_exc() 来定位出错位置 



项目中用一个类来实现了所有的功能，

在 Weibo 类中，首先初始化了一些属性

- cookie 在网络交互中必不可少，需要设置，作者在后续给出了获取 cookie 的方法，即先登录，然后访问该域中任意一个网站，然后就可以查看该请求中携带的cookie 了
- user_id 是待分析的用户的id
- filter 是过滤器，可选择只爬取原创文章或全部文章
- 其他



类中的一些方法：

- 获取用户名：通过访问 https://weibo.cn/user_id/info 可以看到用户信息。 这里使用的是 xpath 来定位元素
- 获取用户信息： 通过访问 https://weibo.cn/u/user_id?filter=0&page=1 查看微博数，关注数和粉丝数。 使用 xpath 来定位元素，re 正则模块来匹配数字



获取微博信息是最重要的一环，其中有一个写法我是第一次遇到

```python
			str_t = info.xpath("div/span[@class='ctt']")
    		weibo_content = str_t[0].xpath("string(.)").replace(u"\u200b", "").encode(
                sys.stdout.encoding, "ignore").decode(
                sys.stdout.encoding)
```

info 是匹配到的某一篇文章，str_t 匹配到文本所在的 span 标签，用 `xpath("string(.)")` 提取出文本字符串，`\u200b` 是一种 HTML 中经常出现的不可见分隔符，需要去掉，最后的一步，转换成了系统标准输出的编码，现在还不清楚xpath string 返回的是什么编码格式的字符串，但感觉这种写法就很稳健不会出错的样子，先记下



然后有一些子函数用于获取所有微博内容，比如有的微博文字太多显示不全，会在页面中显示一个链接阅读全文。有的微博是转发别人的，就需要跟进 url



获取微博发布位置，个人认为是一个很蠢的函数，原先以为就是判断微博是来自iPhone8，来自华为荣耀7，还是来自小米6子类的，后来发现这是另一个函数干的事情，即获取微博发布工具



获取微博发布时间类似



获取所有微博内容首先需要访问 博主的主页，然后搜索有多少页，然后对于每一页有若干条微博，一一进行匹配，对每一条微博，再去匹配信息。 每个步骤单独写一个函数，看起来很舒服



最后是写入文件，使用 os.path 操作文件夹

```python
file_dir = os.path.split(os.path.realpath(__file__))[
    0] + os.sep + "weibo"
if not os.path.isdir(file_dir):
    os.mkdir(file_dir)
file_path = file_dir + os.sep + "%d" % self.user_id + ".txt"
```

之前解码使用系统标准输出的编码格式进行解码成字符串，这里写入文件之前仍然使用该格式进行编码



类提供了一个函数 start ，运行后就会执行所有步骤。