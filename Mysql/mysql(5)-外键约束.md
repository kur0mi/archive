外键在两个数据表间建立关联

```mysql
create table t25(id int primary key);
create table t26(id int primary key, foreign key(id) references t25(id));
create table t26(id int primary key, constraint CustomName foreign key(id) references t25(id));
```

这里在 t26 中定义某字段为外键，并关联到了 t25 的id 字段

我们称 t25 是主表，t26 是从表

还可以在创建表之后，使用 alter 字句修改

```MYSQL
create table t27(id int primary key);
alter table t27 add foreign key(id) references t25(id);
alter table t27 add constraint CustomName foreign key(id) references t25(id);
```

删除 外键约束

```mysql
# 首先查看外键名
show create table t27 \G
alter table t27 drop foreign key t27_ibfk_1;
alter table t27 drop constraint t27_ibfk_1;
alter table t27 drop foreign key CustomName;
```



