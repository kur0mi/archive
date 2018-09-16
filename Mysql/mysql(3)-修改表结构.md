alter 命令用来修改表结构

```mysql
# 添加，删除 字段
alter table t1 add age int;
desc t1;
alter table t1 add age int first;
alter table t1 add age int after id;
alter table t1 drop age;

# 修改表的字符编码
alter table t1 convert to charset set gbk;
show create table t1;

# 重命名 字段
alter table t1 change id uid int;
```

