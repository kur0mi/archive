之前我们创建了一个一个的 Item，然后通过 Item 的 dict API 我们可以手动的填充新的数据。

现在，Item Loader 提供了一个更简便的方式，它是一种填充数据的机制。把数据自动的填入 Item。



```python
from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
	l = ItemLoader(item=Product(), response=response)
	l.add_xpath('name', '//div[@class="product_name"]')
	l.add_css('stock', 'p#stock')
	l.add_value('last_updated', 'today')	# literal value
    return l.load_item()
```



