#### 安装

`pip install virtualenv`

 

#### 使用

```shell
# -p 选项指定 解释器的路径，test-env 是创建的虚拟环境的名称
virtualenv [-p python3] test-env
cd test-env
 
# windows （需要 cmd 环境，需要指定 Scripts 路径）
Scripts\activate
Scripts\pip list
Scripts\deactivate

# linux （激活环境后 pip 等命令可直接使用）
source bin/activate
pip list
deactivate

# 导出与恢复
pip freeze > requirements.txt
pip install -r requirements.txt
```

