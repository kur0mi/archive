这里有多个 shell 可供选择，可以在 scrapy.cfg 中设置环境变量来指定

```shell
[settings]
shell = bpython
```



运行一个 scrapy shell

`scrapy shell <url>`



scrapy shell 支持本地文件，相对路径/绝对路径/file协议都可以



我一般用来测试提取数据：

即在 scrapy shell 下， `response.css().extract_first()` 