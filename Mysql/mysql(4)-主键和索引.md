在mysql中，一张表可以有一个或多个主键（primary key），主键能唯一标识一条记录

在 insert 插入数据时如果主键字段已经存在，会报错

主键经常搭配 自增长（auto_increment）属性 一起使用，一张表只可以有一个自增长属性的字段。且只可以给 主键或索引（index/key） 字段添加 自增长属性。



```mysql
# 将某一字段定义为主键 有两种方式
create table t1 (
	id int primary key, 
    name char(30)
);
create table t1 (
	id int, 
    name char(30),
    primary key(id)
);

# 自增长
create table t1 (
	id int auto_increment primary key, 
    name char(30)
);
```



通过索引，可以加快数据查找速度，主键也是一种索引类型

索引（index/key）有以下几种

```mysql
# 普通索引
"[+] 标识一个普通索引用 key 索引名称(被索引的字段)
 [+] 一般索引名称与被索引的字段名相同即可
 [+] tx(6) 标识以 前6个字符 作为索引
"
create table t1 (
	id int, 
    tx text, 
    key id(id)
);
create table t1 (
	id int, 
    tx text, 
    key tx(tx(6))
);

# 主键索引，又叫主键，主键约束
"[+] 标识主键索引用 primary key(被索引的字段)
"
create table t1 (
	id int, 
    tx text, 
    primary key(id)
);
create table t1 (
	id int primary key, 
    tx text
);

# 唯一索引，又叫唯一约束，unique约束
create table t1 (
	id int, 
    tx text, 
    unique key(id)
);
create table t1 (
	id int unique key, 
    tx text
);

# 全文索引
"[+] 全文索引需要 mysql 版本 5.6+
 	 用 select version()； 查看版本号
"
create table t1 (
	id int, 
    tx text, 
    fulltext key tx(tx)
);

# 多列索引
"[+] key 多列索引名称(字段1， 字段2, ...)
 [+] 只要多列索引中位于开头的那些数据包含在 where 中，
 	 比如 key mk(a, b, c) 只要 a / a and b , mysql 就会主动去使用多列索引查询
"" 使用 explain 查看后边的 select 语句使用了哪些索引
"
explain select * from t1 where firstname="J" and lastname="Mike"; 
```



```mysql
# 查看表索引信息
show index from t1 \G

# 删除索引
drop index tx on t1;
alter table t1 drop index tx;
alter table t1 drop primary|unique key;

# 添加索引
alter table t1 add key id(id);
alter table t1 add index id(id);
alter table t1 add primary key(id);
alter table t1 add unique key(id);
alter table t1 add fulltext key(id);
alter table t1 add key(col1, col2, ...);
```



