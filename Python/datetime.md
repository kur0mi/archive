datetime 是 python 内置模块

```python
>>> from datetime import datetime
>>> s = datetime.now()
>>> e = datetime.now()
>>> e-s
datetime.timedelta(0, 9, 118266)
>>> (e-s).total_seconds()
9.118266
```

