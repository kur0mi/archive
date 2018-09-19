Items 用来结构化数据

创建 Item

```python
import scrapy

class Product(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	stock = scrapy.Field()
	last_updated = scrapy.Field()
```



Item 封装了 dict，并且 Item 额外提供了 fields 属性。

需要注意的是，fields 包含该 Item 声明时的所有字段，而 keys 仅包含实例化类时被填充的那些字段。

```python
product = Product(name='PC', price=100)
product = Product({'name':'PC', 'price':100})
product['name']
product.get('name', 'not set')
'name' in product
'last_updated' in product.fields
product.keys()
product.items()
product2 = product.copy()
```



扩展或修改一个 Item，使用继承

```python
class DiscountedProduct(Product):
	discount_percent = scrapy.Field(serializer=str)
```



