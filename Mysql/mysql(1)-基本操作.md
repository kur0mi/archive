1. 创建，删除，查看，备份，还原

   ```mysql
   "创建与删除"
   "[+] 操作数据库"
   create database db;
   show databases;
   show create database db;
   drop database db;
   "[+] 操作数据表"
   use db;
   create table t1 (
       id int, 
       name char(30)
   ) engine=innodb charset=utf8;
   show tables;
   desc t1;
   show create table t1;
   drop table t1;
   
   
   "备份与还原"
   "[+] 可以用来重命名数据库"
   "[+] 还原之前需要提前创建好数据库"
   "[+] 远程备份还原可以使用 -h 选项"
   mysqldump -uroot -p db > db.sql;
   mysqldump -uroot -p db < db.sql;
   
   
   "备份还原数据表"
   mysqldump -uroot -p db t1 > db_t1.sql;
   mysqldump -uroot -p db < db_t1.sql;
   
   "重命名数据表"
   rename table t1 to t2;
   ```


