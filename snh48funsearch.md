# SNH48 xox info search

## 表设计

字段不为null，default

mysql 8.0

### 1. 成员表 

> member_info

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|name|姓名|
|nickname|昵称|
|catchphrase|历史口号 json，会变化|
|catchphrase|最新口号 ，会变化|
|hometown|籍贯|
|birth|生日|
|age|年龄|
|grade|期数|
|debut_time|出道时间|
|graduate_time|毕业时间|
|status|状态：nomal，quit，rest，graduted，预备（数字表示），会变化|


### 2. 队表

> team_info

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|name|队名|
|city|所在城市|
|start_time|创建时间|
|disband_time|解散时间|
|status|状态：正常，解散|


### 3. 队-成员表

> team_member

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|team_id|队id|
|xox_id|成员id|
|status|状态，成员和队的关系状态，0失效，1有效|
|join_in_time|进队时间|
|out_time|离开时间|
|role|普通，队长，副队|


### 4. 总选表 

> election_info

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|year|举办时间|
|xox_id|xox名字[foreign key: xox_info]|
|rank|排名|
|tick_count|票数|

### 5. B50节目表

> b50_info

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|name|节目名称|
|year|年度|
|tick_count|票数|
|rank|排名|

### 6. B50节目-成员表

> b50_member

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|xox_id|成员id|
|b50_id|节目id|


### 7. 公演表

> show_info

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|time|举办时间|
|name|公演名称|
|team|所属队，json能否实现记录多个队{team:[team_id1, team_id2]}|
|unit|unit名单|
|mc|mc话题|


### 8. 公演-成员表

> show_member

|字段|含义|
|----|----|
|id|自增编号[primary key]|
|xox_id|成员id|
|show_id|公演id|


## 技术栈

python+flask+mysql8.0 后端

vue + ElementUI 前端

nginx 部署

## 其他


elastic search 搜索引擎

图数据库


### 查询

第一版：限制查询成员，队名

查询1：

李艺彤-》个人信息，所在队的信息（可跳转到队），历届总选信息，历届参与的b50信息，参与最近50场公演

查询2：

SII-》队信息，队所有成员的名字（可跳转成员），最近50场公演

模糊查询：

李-》所有李的关联列表（可跳转）


### 数据库更新

数据更新限制：

成员表，队表，成员-队关系表  单条修改，批量修改 3×2个入口

有些数据限制不需更新，需要管理员确认


### 登陆模块






