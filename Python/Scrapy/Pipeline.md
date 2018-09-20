pipeline 负责处理解析后返回的 Items 



#### pipeline

pipeline 必须实现以下几个方法

> process_item(self, item, spider)

对每个 item 都将调用 process_item 方法，返回值 或者是 一个字典，或者是 item，或者抛出 DropItem 异常，则该 Item 不再被后续的 pipeline 处理。



#### 校验和调整

```python
from scrapy.exceptions import DropItem

class PricePipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)
```



#### 存储

```python
import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
```



#### 存入 Mongo 数据库

```python
import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
```



这里是 from_crawler 的使用方法，如果这个类方法存在，它返回一个新的管道实例

这里提供了 crawler 访问 pipeline 组件的方式，根据官方文档，crawler 可以访问到所有的 scrapy 组件



