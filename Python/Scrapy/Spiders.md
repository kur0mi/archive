#### Spiders

爬虫定义了一组规则，如何去爬行，如何提取数据

爬虫是一个循环：

1. 对于给定的 start_urls，生成最初的请求（Requests），并且指定一个回调函数。请求后返回的响应（Response）作为参数，被回调函数处理。
2. 在回调函数中，解析响应（Response）然后返回结构化的数据，Item，或新的 Request
3. 在回调函数中需要解析响应（Response），一般使用 选择器（Selector）来解析数据，当然也可以使用 BeautifulSoup，lxml 等，然后使用 Item 来提取数据
4. 最后，返回的 Items 通过 管道（Item Pipeline）被保存到数据库中，或者通过 Feed exports 写入文件。



#### scrapy.Sider

这是最简单的爬虫类，我们定义的的爬虫必须继承它。

它提供了默认的 `start_requests()` 实现，在该函数中使用了 start_urls 作为起始 URL，返回一组 Request，这些 Request 默认调用回调函数 `parse()` 

Spider 还提供一个 name 属性，可以标识这个爬虫。

> allowed_domains

设置允许爬虫爬取的域名。需要开启 OffsiteMiddleware 中间件

> start_urls

被 start_requests() 使用

> custom_settings

> crawler

> from_crawler()

> settings

> logger
>
> log(message)
>
> parse(response)
>
> closed(reason)



#### 传参

Spider 默认的 `__init__()` 方法解析 `-a` 选项指定的参数，并拷贝作为 spider 的属性

注意，这些参数类型均为字符串，spider 对它不做任何处理。

较复杂的参数可以使用 `json.loads` 自定义处理。或者 schedule.json API

传参可以用来设置 HttpAuthMiddleware 使用的认证参数或 UserAgentMiddleware 使用的 user agent 参数

`scrapy crawl myspider -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot` 



Scrapy 附带了一些常用的爬虫。在一些常见的情景下快速处理，比如

- 基于特定规则追踪一个站点的所有链接
- 基于 Sitemaps 进行爬行
- 解析 XML/CSV

 CrawlSpider，XMLFeedSpider，CSVFeedSpider，SitemapSpider 等等