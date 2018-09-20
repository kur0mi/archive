Scrapy 提供了一个 `scrapy` 的命令行工具。使用 scrapy ，你可以轻松管理你的爬虫项目。



#### Configuration settings

/etc/scrapy.cfg 是系统范围内的配置

~/.config/scrapy.cfg 是用户范围内的配置

项目的配置文件是 `scrapy.cfg` ，在项目根目录下

同时，scrapy 也支持一些环境变量的设置，比如 `SCRAPY_SETTINGS_MODULE` , `SCRAPY_PROJECT` `SCRAPY_PYTHON_SHELL` 



#### scrapy 工具的使用

`scrapy`

`scrapy startproject myproject [project_dir]` 创建项目

`scrapy genspider mydomain mydomain.com` 

全局范围内的 scrapy 工具

- [`startproject`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-startproject)
- [`genspider`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-genspider)
- [`settings`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-settings)
- [`runspider`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-runspider)
- [`shell`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-shell)
- [`fetch`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-fetch)
- [`view`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-view)
- [`version`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-version)

在项目内，使用 spider 管理你的项目

- [`crawl`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-crawl)
- [`check`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-check)
- [`list`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-list)
- [`edit`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-edit)
- [`parse`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-parse)
- [`bench`](https://doc.scrapy.org/en/latest/topics/commands.html#std:command-bench)

