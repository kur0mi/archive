EIGRP 特点：

- CISCO 私有
- 无类路由协议，支持 VLSM
- 使用 DUAL 算法，形成 无环路由
- 快速收敛，有后继和可行后继
- 低路由更新开销，支持组播及单播方式
- 支持自动/手工汇总
- 支持等价/非等价负载均衡
- 支持多种网络层协议



EIGRP 有三张表

1. 邻居表
2. 拓扑表
3. 路由表



配置

```
conf t
	router eigrp autonomous-system-num
	network network [wildcard-mask]
	
```

