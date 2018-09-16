select 查询记录

```mysql
select * from t1;
select id, name from t1;
```



insert 用来在表中插入一行数据

```mysql
insert into t1 (id, name)
	values (1, "first one"), (2, "second one");
```



update 用来修改记录

```mysql
update t1 set id=3 where name="first one";
```



delete 删除记录

```mysql
delete from t1 where id=1 or id=2;
```

