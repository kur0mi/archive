`logging` 是 python 的内置模块



```python
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
```



默认情况下，日志输出到屏幕，日志级别为 WARNING，日志格式为 `日志级别：Logger实例名称：消息内容`，如 `WARNING:root:warn message` 



#### 日志级别

| 级别     | 何时使用                   |
| -------- | -------------------------- |
| DEBUG    | 调试信息，调试时才会感兴趣 |
| INFO     | 一切按预期运行             |
| WARNING  | 警告，可能会出问题         |
| ERROR    | 错误，已经出现一些问题     |
| CRITICAL | 严重错误                   |



#### 简单配置

`logging.basicConfig(filename='logger.log', level=logging.INFO)` 

配置之后，输出方式被定向到 filename，日志级别为 INFO