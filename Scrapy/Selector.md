#### 部分CSS 选择器语法

| 选择器          | 示例       | 示例说明                     |
| --------------- | ---------- | ---------------------------- |
| .class          | .intro     | 所有class="intro" 的元素     |
| #id             | #firstname | 所有id="firstname" 的元素    |
| */-             | *          | 所有元素                     |
| element         | p          | 所有<p>元素                  |
| element,element | div,p      | 所有<div>元素和<p>元素       |
| element element | div p      | 所有<div>元素内的<p> 元素    |
| element>element | div>p      | 所有父级是<div>元素的<p>元素 |
| element+element | div+p      | 所有紧接着<div>元素的<p>元素 |



#### Selector

selector 是 scrapy 的一个组件，基于 lxml 开发，用来从 HTML 或 XML 中提取信息

使用 `Selector(text=body)` 或 `Selector(response=response)` 

更一般的，我们使用 `response.selector` 来访问到选择器



#### Using Selector

通过 selector 的 `.css()` 或 `.xpath()` 方法来进行选择，可以直接简写为 `response.css()` 和 `response.xpath()` ，返回包含 `Selector` 对象的 类列表 -- `SelectorList` 对象

调用 SelectorList 对象的 `extract()` 方法获取所有提取到的的数据，通过 `extract_first()` 仅获取第一个，如果找不到任何元素，`extract_first()` 返回 `None`，或者可以手动设置默认值 `extract_first(default='not-found')` 

`css('title::text')` 可以选择伪元素

一定注意：`css() 和 xpath()` 是 Selector 的方法。



#### Regular expressions

`re()` 是 Selector 的方法，不同的是，它返回的是 字符串

`re_first()` 返回第一个结果



