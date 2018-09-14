### GNS3 安装配置

1. 模拟器简介

   GNS3 是思科的模拟器，用来模拟路由器，交换机和防火墙等网络设备，由于实体设备的昂贵，使用模拟器就成为了做网络实验和网络学习的首选。但需要注意的是，模拟器和实体设备仍然存在许多差异。不过在网络学习的初期入门阶段使用模拟器是完全没有问题的。

   另外还有两款其他公司开发的著名的模拟器软件：

   华为 - eNSP

   华三 - H3C Cloud Lib

2. Cisco 网络设备结构

   - ROM - 只读存储器，存放启动程序，POST（上电自检）程序。此外还有一个mini版的 ios
   - flash - 闪存，相当于计算机的硬盘，存放 IOS（网际操作系统）。开机时加载的配置文件也放在这里（在一些旧设备中，配置文件放在 nvram 中，新式设备移除了 nvram）。还包括其他一些东西，web页面等等。
   - RAM- 随机读取存储器，断电丢失，拷贝 IOS 并运行。

3. 登陆到网络设备

   新购置的网络设备，在初次调试时，会使用笔记本 经由 console 线和 USB-RS232转接线（需安装驱动）连接到设备的 console 口。驱动程序将一个USB接口模拟为COM接口，在设备管理器->串行总线控制器 得到COM端口号，然后用终端软件通过 serial（串口）协议就可以登录到设备。

   下边说一下虚拟的设备。预先将各种 IOS 放在 gns3 虚拟机中，并分别映射到虚拟机的不同端口。通过 telnet 即可登陆到设备，实际相当于通过 console 口登陆。

4. 安装

   环境 win10，64位操作系统，x64处理器

   版本 GNS3 v2.1.8

   1. 软件准备

      在GNS3官网下载 GNS3-2.1.8-all-in-one.exe 主程序

      在官网下载 GNS3.VM.VMWare.Workstation.2.1.8.zip 虚拟机镜像（和主程序版本一致）

      解压后，取出 GNS3 VM.ova 文件

      Cisco IOS（Interwork Operating System） 镜像文件

      - 可以自己在网上找一些常用的 IOS，也可以使用下边我用的
      - [我的网盘链接：包含license许可文件和路由器交换机ios各一个](https://pan.baidu.com/s/1cXh6dnWWyKOrW0ac5q1Y-w) （密码：jl3v）

   2. 安装 vmware 虚拟机，导入 GNS3 VM.ova，将创建一个名为 GNS3 的虚拟机

   3. 运行 gns3-all-in-one（右键管理员权限运行）

      组件选择（记不清了.. 把推荐的都选上吧 winpcap, wireshark, dynamips, qemu, vpcs, cpulimit, gns3。 除了 solaris 那个其他都选）

      - winpcap win平台用于模拟网络通信，必选
      - wireshark 用于抓包，推荐
      - dynamips qemu vpcs 是模拟器，都选上吧
      - cpulimit 可以降低cpu占用，必选
      - solaris 啥的是用于分析抓到的包，非必选，用 wireshark也可以分析
      - gns3 主程序，必选

   4. 连通 gns3 和 虚拟机

      - 启动 GNS3，出现 setup wizard，默认选第一项，勾选 dont show again
      - 点击下一步，默认绑定服务器地址 127.0.0.1
      - 等待连接到本地服务器
      - 配置虚拟机（选择自己的 GNS3 VM，1 核心，2048M 内存）
      - 等待虚拟机自动启动
      - 选择不导入镜像文件
      - 结束

   5. 导入镜像（edit->preference）

      gns3 支持多种模拟器镜像

      - dynamips 模拟器（不推荐）：将镜像下载到本地（镜像类似 c2600-xxx.bin 这种格式），占用资源非常多！

      - IOU 模拟器（推荐）：镜像放在vm虚拟机里（i86bi-xxx.bin）

        解压上边网盘里的 IOU-IOS.rar，取出 三个文件

        点击 ios on unix，选择导入 iourc 许可文件

        [ios on unix->iou devices] 添加设备

        - 选择在虚拟机运行
        - 选择 L2 image，导入 交换机镜像（带 l2 的）
        - 选择 L3 image，导入 路由器镜像

      - 在左侧，选 available devices，可以看到刚才导入的ios

5. 出错解决

   - gns3 invalid auth for server vm

     进入 gns3 vm 虚拟机，security 选择 不需要认证

 

### 简单实验

每台网络设备（路由器，交换机等）都有一个 console，用于在初次上电时进行调试

在实体设备中，我们需要用 console 线和 USB-RS232 转接线将设备与笔记本相连，然后用终端管理软件（通过 serial 串口协议）连接到设备

但是在 gns3 虚拟设备中，我们是通过 telnet 协议连接到 设备的

1. 搭建小型网络拓扑

   1. 从左侧拖入两个 路由器，用网线连接，记下连接的接口（这里选择 Ethernet0/0）
   2. 启动设备

2. 路由基础

   实验环境下推荐预先配置一些东西用于提高效率

   ```shell
   conf t                # 进入全局配置模式
   	hostname R1            # 修改主机名
   	line console 0        # 进入 console 口
   	no exec-time        # 防止由于长时间未操作而导致设备退出
   	logging synchronous    # 防止输入被日志打断
   	exit               
   no ip domain lookup    # 特权模式下键入非关键字符时，会进行dns解析影响效率
   ```

   分别为两个接口（Ethernet 0/0）配置 ip

   R1：

   ```shell
   en
   	conf t        			# 全局配置模式
   		int e 0/0    		# 进入以太网口 0槽 0口
   		ip addr 192.168.12.1 255.255.255.0    # 配置 ip 和掩码
   		no shutdown    		# 开启该接口
   		exit
   	exit
   sh ip int brief    			# 显示设备接口的ip信息
   ```

   最后应该看到 ip配置准确，且 status（物理状态）up，protocal（协议状态）up

   同理为 R2 配置 ip 192.168.12.2/24

   进行 ping 测试

3. 配置 console 登录密码，serial（串口）协议连接到设备的 console 口（或虚拟设备用 telnet 连接到 console 口）时进行密码认证

   ```shell
   # 在特权模式下
    
   conf t
   line con 0            # 进入 console 口
   password console    # 设置密码
   login                # 启用登陆认证
   exit
   exit
   write                # 保存配置
   ```

4. 配置 enable（特权）密码，从用户模式进入特权模式时进行密码认证

   ```shell
   # 在特权模式下
    
   enable secret enpassword    # 配置密文密码
   no enable secret            # 取消 特权密码
   ```

5. telnet 密码，用于远程通过 telnet 登陆到设备时进行密码认证

   ```shell
   # 在特权模式下
    
   line vty 0 4    # 开启5个虚拟会话通道
   password vtypassword    # 密码
   login                # 开启密码认证
   exit
   ```

6. telnet 连接测试

   尝试从 R1 telnet 到 R2，发现不通 `% refused by remote host`，查看配置文件 `show running-config` ，发现 `transport input none`

   解决方案，在进入 vty 通道后，键入 `transport input telnet` 开启 telnet 认证

7. 记得在特权模式下键入 `write` 保存配置，否则断电后配置将丢失

 