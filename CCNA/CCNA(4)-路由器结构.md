##### 路由器组成

- ROM - 只读存储器，断电后内容不会丢失，用来存放那些一般不会改动的东西，比如引导程序（Bootstrap）。此外还有一个 mini 版的 IOS（Internet Operate System，网际操作系统），用于在 IOS 损坏设备无法正常启动时提供诊断和修复之类的功能
- flash - 闪存，相当于计算机的硬盘，断电后内容不会丢失，存放 IOS。开机时加载的配置文件（Start-up config）也放在这里（在一些旧设备中，配置文件放在 nvram 中，新式设备移除了 nvram）。此外还包括其他一些东西，比如一些路由器提供的web页面等等。
- RAM - 随机读取存储器，断电丢失，用于存放临时的指令和数据，速度很快
- Interface - 接口，用来连接外部设备。可以配置为多种模式，如 access（接入）, trunk（干线） 等



##### 路由器启动过程

1. 执行加电自检（POST, Power-On Self Test）： 设备上电后，会执行一些检测来测试硬件是否可以正常工作。随后把 Bootstrap 加载到 RAM

1. 执行引导程序（Bootstrap）：引导程序会定位 IOS，并将 IOS 加载到 RAM 中，之后把控制权交给 IOS（IOS 可能位于 闪存或TFTP服务器上）
2. IOS 会寻找启动配置文件（Start-up config），找到后将其复制到 RAM 中作为 运行配置（Running config），并用此配置来启动路由器。如果没有找到则进行初始化配置



##### IOS 备份及恢复实验

待续...