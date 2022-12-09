## reference
[link](https://aaronice.gitbook.io/system-design/system-design-systematic-approach)

### 1) Requirements and Goals

- Functional Requirements
- Non-Functional Requirements
- Extended Requirements

### 2) Capacity Estimation and Constraints
- Traffic estimates: load balance, queue
- Bandwidth estimates: 
- Memory estimates: sharding, cdn, replica

### 3) System APIs

### 4) Database Design
- Database Schema
- Data flow  ->  data partitioning, Replication /


### 5) evolution

Partitioning, Replication

Cache

Load Balancer (LB)

Security and Permissions

---

系统设计基本方法 SNAKE 原则 by Qingyuan Feng
系统设计有四大要素
第一，是要满足一个需求即Requirements；
第二，对内容进行一个定义；
第三，从不同维度去考虑宏观的架构层、组件层、模块层；
第四，也要考虑到互相间交流的接口和相关传递的数据。所以这些内容一起构成了整个系统设计。
系统设计的基本方法 — SNAKE原则（Scenario, Necessary, Application, Kilobit, Evolve）
Scenario（场景）：用例Use Case/接口Interface
Necessity（限制）：查看需求Requirement/假设Assumption
Application（应用）：服务Service/算法Algorithm
Kilobit（数据）Data
Evolution（进化）
http://blog.bittiger.io/post180/
系统设计九阴真经: 4S 分析法
Scenario 场景
需要设计哪些功能，设计得多牛（需要承受多大的访问量 DAU / MAU）
Ask / Features / QPS / DAU / Interfaces
Ask
Step 1: Enumerate 罗列功能
Step 2: Sort / Rank 选出核心功能
Analysis & Predict
并发用户 Concurrent User
日活跃 * 每个用户平均请求次数 / 一天多少秒 （e.g. 150M * 60 / 86400 ~ 100k QPS）
峰值 Peak = Average Concurrent User * 3 (normally 2~ 9 times of average) (~300k QPS) 
快速增长的产品  Fast Growing 预测
MAX peak users in 3 months = Peak users * 2
读频率 Read QPS (Queries Per Second)
300k
写频率 Write QPS 
5k
给人用的产品一般读多写少，给机器用的一般读少写多
R PS < DB PS < IO PS
QPS = 100
用自己的笔记本
QPS = 1k
服务器
QPS = 1M
1000台服务器集群
QPS和 Web Server (服务器) / Database (数据库) 之间的关系
一台 Web Server 约承受量是 1k 的 QPS （考虑到逻辑处理时间以及数据库查询的瓶颈）
一台 SQL Database 约承受量是 <1k 的 QPS（如果 JOIN 和 INDEX query比较多的话，这个值会更小）
一台 NoSQL Database (Cassandra) 约承受量是 10k 的 QPS 
一台 NoSQL Database (Memcached) 约承受量是 1M 的 QPS
Service 服务
将大系统拆分为小服务
Split / Application / Module
步骤
Step 1: Replay
重新过一遍每个需求，为每个需求添加一个服务
Step 2: Merge
归并相同的服务
什么是 服务Service?
可以认为是逻辑处理的整合
对于同一类问题的逻辑处理归并在一个Service中
把整个System细分为若干个小的Service
Storage 存储*
数据如何存储与访问
Schema / Data /SQL / NoSQL / File System
步骤
Step 1:Select
•为每个Application / Service选择合适的存储结构
Step 2:Schema
•细化数据表结构
类型
数据库系统Database
关系型数据库SQL Database
用户信息User Table
非关系型数据库NoSQL Database
推文Tweets
社交图谱Social Graph (followers)
文件系统File System
图片、视频Media Files
缓存系统Cache
不支持数据持久化Non-persistent 
效率高，内存级访问速度
Scale 升级
解决缺陷，处理可能遇到的问题
Sharding / Optimize / Special Case
Step 1: Optimize
解决涉及缺陷 Solve Problems
Pull vs Push
更多功能设计 More Features
Like， Follow& Unfollow, Ads
一些特殊情形
Step 2:Maintenance
鲁棒性Robust
如果有一台服务器/数据库挂了怎么办
扩展性Scalability
如果有流量暴增，如何扩展
什么时候用Push
资源少
少写代码
实时性要求不高
用户发帖比较少
双向好友关系，灭有明星大v问题（比如朋友圈）
什么时候用Pull
资源充足
实时性要求高
From Hired in Tech System Design Course
https://www.hiredintech.com/classrooms/system-design
Step 1: Constraints and Use Cases
Figuring out scope, use cases, gather requirements about the system.
Estimates, constraints of the system.
Step 2: Abstract Design
Outlining a high-level abstract design:
Simple diagram, main components, connections between them.
Step 3: Understanding Bottlenecks
Step 4: Scaling Your Abstract Design