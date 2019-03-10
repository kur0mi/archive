##  dada

##  Tools

- lzop
- utf9
- uuencode, uudecode

##  Steps

1.LZOP compress 解压缩
​    lzop -dvN aaa.lzo

2.根据文件名 KJDEGNBQGQZA==== base32后得知是RFC4042
​    也就是utf9， 使用Python 的 utf9 库解密后即可

3.打开文件，是uuencode文件，修复后uudecode即可 

​    需要安装 `apt-get install sharutils` 

4.解开后是一个 jpg，修剪文件头



zip 密码爆破

crc32 爆破

伪加密

