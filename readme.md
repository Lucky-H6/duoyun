"碎片化时间数据标注平台"软件系统架构设计

v0.1 

设计 luckyh6

一、技术概述

​	“碎片化时间数据标注平台”软件系统由四部分组成，分别是(1)前端; (2)后端; (3)数据库系统; (4)文件系统
​	"碎片化时间数据标注平台"软件系统在设计时应遵循基本软件设计原则，并尽量减少在运行维护中直接访问后端服务器的动作。本架构应实现所有用户用例、管理操作所需要的接口，在通过接口进行操作时进行日志记录，以减少对后端数据的不经日志系统的直接操作。

​	(1) 前端系统主要使用html/js/css技术，通过jQuery/AJAX与后端接口进行通信，使用python flask返回界面

​	(2) 后端系统使用python作为开发语言，分为模型和接口两部分。接口部分使用flask进行http请求处理。

​	(3) 数据库系统使用MySQL.

​	(4) 文件系统为ubuntu操作系统文件系统

​	一些说明：

​		task: 发布者发布的一个标注任务

​		work: 标注者每次开始标注一个新的task时，如果目前该标注者没有该task的work, 则生成一个该task的work。当用户每次提交一个work时，结束一个work.

​		publisher:  发布者

​		user: 用户



二、详细说明

1. 前端系统

   前端系统包括9个功能界面和一个404错误界面。具体为：

   (1) 首页(/index/)：

   ​		基本功能：网站宣传，引导登录、注册等操作

   ​		页面组件：

   | 组件名 | 类型        | 描述       | 父元素   | 事件 |
   | ------ | ----------- | ---------- | -------- | ---- |
   | 轮播图 | boot4轮播图 | 宣传图展示 | document |      |

   

   (2) 登录界面(/login/)：

   ​		基本功能：引导用户进行登录

   ​		页面组件：

   | 组件名       | 类型       | 描述             | 父元素   | 事件         |
   | ------------ | ---------- | ---------------- | -------- | ------------ |
   | 选项卡       | boot4 tabs | 选择登录的用户组 | document | 切换登录身份 |
   | 账号输入框   | input      | 用户输入账号     | 选项卡   |              |
   | 密码输入框   | input      | 用户输入密码     | 选项卡   |              |
   | 确认登录按钮 | button     | 点击登录账号     | 选项卡   | /api/login/  |

   

   (3) 注册界面(/register/)：

   ​		基本功能：引导用户进行注册

   ​		页面组件：

   | 组件名         | 类型       | 描述             | 父元素   | 事件                 |
   | -------------- | ---------- | ---------------- | -------- | -------------------- |
   | 选项卡         | boot4 tabs | 选择注册的用户组 | document | 切换注册身份         |
   | 账号输入框     | input      | 用户输入账号     | 选项卡   | /api/check-username/ |
   | 密码输入框     | input      | 用户输入密码     | 选项卡   | 检查密码格式         |
   | 确认密码输入框 | input      | 用户输入确认密码 | 选项卡   | 检查密码是否相同     |
   | 确认注册按钮   | button     | 用户确认注册     | 选项卡   | /api/register/       |

   

   (4) 用户中心界面(/user/center/)：用户登录后的导航场所

   ​		基本功能：用户登录后的导航场所

   ​		页面组件：

   | 组件名           | 类型            | 描述           | 父元素     | 事件               |
   | ---------------- | --------------- | -------------- | ---------- | ------------------ |
   | 左侧导航栏       | boot4 row pills | 子页面分割     | document   |                    |
   | 任务大厅导航     | boot4 nav item  | 进入任务大厅   | 左侧导航栏 | /api/get-task/     |
   | 我的工作导航     | boot4 nav item  | 进入我的工作   | 左侧导航栏 | /api/get-work/     |
   | 账号信息导航     | boot4 nav item  | 进入账号信息   | 左侧导航栏 | /api/get-userinfo/ |
   | 领取奖励导航     | boot4 nav item  | 假导航         | 左侧导航栏 |                    |
   | 任务大厅         | div             | 任务大厅子页面 | document   |                    |
   | 任务大厅搜索框   | input           | 搜索任务       | 任务大厅   |                    |
   | 任务大厅提交搜索 | button          | 搜索任务       | 任务大厅   | /api/get-tesk/     |
   | 任务卡片         | boot4 card      | 展示任务信息   | 任务大厅   |                    |
   | 我要标注         | button          | 进入标注工作台 | 任务卡片   | /work/new/         |
   | 我要审核         | button          | 假按钮         | 任务卡片   |                    |
   | 我的工作         | div             | 我的工作子页面 | document   |                    |
   | 工作卡片         | boot4 card      | 展示工作信息   | 我的工作   | /user/workspace/   |
   | 账号信息         | div             | 账号信息子页面 | document   |                    |
   | 账号信息展示框   | div             | 展示账号信息   | 账号信息   |                    |
   | 申请专业认证     | button          | 假按钮         |            |                    |

   

   (5) 用户标注工作台(/user/workspace/)：

   ​		基本功能：用户进行标注的界面

   ​		页面组件：

   | 组件名       | 类型   | 描述                | 父元素   | 事件        |
   | ------------ | ------ | ------------------- | -------- | ----------- |
   | 工作名       | p      | 工作名展示          | document |             |
   | 标注区       | div    | 进行标注的工作区    | document |             |
   | 标注图片     | img    | 当前正在标注的图片  | 标注区   | （框选）    |
   | 上一张下一张 | button | 切换图片按钮        | 标注区   | /work/get/  |
   | 暂存         | button | 上传本地label到云端 | 标注区   | /work/save/ |
   | 提交         | button | 提交并结束work      | 标注区   | /work/end/  |
   | 提示文字     | p      | 提示信息            | 标注区   |             |
   | 标注工具     | --     | 如输入框等          | 标注区   |             |

   开发时注意：

   + 提交按钮也需要将标注内容存入内存

   

   (6) 发布者中心界面(/publisher/center/)：发布者登录后的导航场所

   ​		基本功能：发布者登录后的导航场所

   ​		页面组件：

   | 组件名       | 类型            | 描述               | 父元素       | 事件                  |
   | ------------ | --------------- | ------------------ | ------------ | --------------------- |
   | 左侧导航栏   | boot4 row pills | 子页面分割         | document     |                       |
   | 我的任务导航 | boot4 nav item  | 进入我的任务       | 左侧导航栏   | /api/get-task/        |
   | 我要发布导航 | boot4 nav item  | 进入我要发布       | 左侧导航栏   |                       |
   | 我的账单导航 | boot4 nav item  | 假导航             | 左侧导航栏   |                       |
   | 我的任务     | div             | 我的任务子页面     | document     |                       |
   | 任务卡片     | boot4 card      | 展示任务信息       | 我的任务     |                       |
   | 结束任务按钮 | button          | 结束任务           | 任务卡片     | /task/end/            |
   | 我要发布     | div             | 我要发布子页面     | document     |                       |
   | 任务类型选择 | image-button组  | 选择任务类型       | 我要发布     | 展开任务模式          |
   | 任务模式选择 | image-button组  | 选择任务模式       | 任务类型选择 | 显示下一步按钮        |
   | 下一步按钮   | button          | 进入任务设计工作台 | 我要发布     | /publisher/workspace/ |

   

   (7) 任务设计工作台(/publisher/workspace/)：

   ​		基本功能：发布者进行任务设计的界面

   ​		页面组件：

   | 组件名         | 类型   | 描述           | 父元素   | 事件                          |
   | -------------- | ------ | -------------- | -------- | ----------------------------- |
   | 资料上传       | div    | 任务资料上传   | document |                               |
   | 上传任务指导书 | input  | 上传任务指导书 | 资料上传 | /api/upload-task-instruction/ |
   | 上传数据集     | input  | 上传数据集     | 资料上传 | /api/upload-dataset/          |
   | 设计区         | div    | 任务设计区     | document |                               |
   | 设计区内部组件 | --     | 设计区内部组件 | 设计区   | --                            |
   | 提交任务       | button | 提交任务按钮   | 设计区   | /task/new/                    |

   ​
   补充说明：task, work卡片一共三处需要，卡片提供信息为：
   
   + 任务大厅：task名称、发布者、完成进度、专业技能
   + 历史标注：task名称、发布者、完成张数、专业技能
   + 我的任务：task名称、完成进度、专业技能

2. 后端系统

   2.1 接口

   ​	所有接口应实现以下公共参数：

   ​		status: unsigned int, 代表任务执行的状态值

   ​	所有可能的状态值如下：

   ​		0: succeed

   ​		1: failed

   ​		2: authentification failed,need login

   ​		500: internal error

   

   ​	系统应实现以下接口

   ​	2.1.1 /api/login/

   ​	用于登录的POST接口。

   ​	请求参数：

   ​		username: 用户名

   ​		password: 密码

   ​	响应参数：

   ​		user-group: int 用户组，0: 普通用户， 1: 任务发布者， -1: 错误

   ​		(添加cookie)

   ​	

   ​	2.1.2 /api/check-username/

   ​	用于检查用户名是否已经被注册的GET接口

   ​	请求参数：

   ​		username: 用户名

   ​	响应参数：

   ​		occupied: boolean 0为未注册，1为已注册

   ​	

   ​	2.1.3 /api/register/

   ​	用于注册用户的POST接口

   ​	请求参数：

   ​		username: 用户名

   ​		password: 密码

   ​		re_password: 确认密码

   ​	响应参数：

   ​		user-group: int 用户组，0: 普通用户， 1: 任务发布者， -1: 错误

   

   ​	2.1.4 /api/get-task/

   ​	用于任务检索的GET接口

   ​	请求参数：

   ​		type: 任务检索的类型

   ​				0：用户中心任务大厅通过任务名进行检索

   ​				1：发布者我的任务，通过发布者和任务名进行检索

   ​		content: 检索的任务名内容

   ​	响应参数：

   ​		tasks: dict 任务的信息

   

   ​	2.1.5 /api/upload-task-instruction/

   ​	上传任务指导书的POST接口

   ​	请求参数:

   ​		file: 上传的文件

   ​	

   ​	2.1.6 /api/upload-dataset/

   ​	上传数据集的POST接口

   ​	请求参数:

   ​		file: 上传的文件

   

   ​	2.1.7 /api/get-work/

   ​	用户获取历史标注的接口。

   ​	响应参数：

   ​		works:  dict  历史work的json

   

   ​	2.2  模型

   ​	2.2.1  Task类

   ​		属性: 

   - task_id:  任务id

     - publisher: 发布者id

     - task_name: 任务名

     - type:  任务类型

     - mode:  任务模式

     - rate_of_process:  进度

       方法:

   - \_\_init\_\_(task_id): 构造函数, 连接数据库并获得任务信息

   - create_task(publisher, task_name, type, mode): 类方法, 创建项目

   - get_task(publisher=None, content=None): 类方法, 根据发布者id和任务名查询任务, 返回任务id列表

   

   ​	2.2.2  User类

   ​		属性: 

   - username: 用户名

   - password: 密码

   - user_type: 用户类型

     方法:

   - \_\_init\_\_(user_name, password, user_type): 构造方法, 摘要密码, 写入数据库

   

   ​	2.2.3  Work类

   ​		属性:

   - work_id: work id

   - user_id: 标注该任务的用户id

   - task_id: 该任务的id

   - work_status: 0为工作中, 1为已完结

     方法:

   - \_\_init\_\_(work_id): 构造方法, 连接数据库并获得work信息

   - get_works(user_id): 类方法, 连接数据库并返回全部value为1的work_id列表

   - check_task(task_id): 类方法, 检查用户有无该task下未完成的work. 有则返回work_id, 无则返回None.

   

   ​	2.3  数据库

   ​		数据库中共包含4张表，分别为：

   ​		2.3.1  tasks表

   ​			发布者每次发布任务时，增加一条记录

   ​			task_id int primary_key auto_increment	task的唯一标识

   ​			publisher int not null	task发布者id

   ​			task_name varchar(32)  not null   task名称

   ​			type tiny_int not null   task类型，0为图片，1为语音，2为文字

   ​			mode tiny_int not null    task模式，对于图片来说，0为元素框选，1为元素描述，2为手工分类

   ​		2.3.2  data_url表

   ​			发布者每次发布任务时，将上传的dataset中全部内容导入

   ​			data_url  varchar(128)  数据的地址

   ​			status  tiny_int    数据的状态，0为未分配，1为工作中，2为待审核，3为已完成
   
            work_id  int   分配给了哪个work_id

   ​		2.3.3  user表

   ​			user_id  int  primary_key  auto_increment    user的唯一标识

   ​			username   varchar(32)   用户名

   ​			password    varchar(128)   密码（经过md5摘要）

   ​			user_type   tiny_int   0为普通用户，1为发布者

   ​		2.3.4  works表

   ​			用户每次点击任务大厅的task进入标注时，若用户没有该task的work，则创建一个该task的work。当用户与标注工作台点击提交时，结束一个任务

   ​			work_id int primary_key auto_increment     work的唯一标识

   ​			user_id  int 	标注者标识

   ​			task_id   int     任务标识

   ​			value   tiny_int   1为开始任务,  -1为结束任务

   ​			operation_time  datetime   操作时间

   ​		

   2.4  文件系统

   |___data

   ​	   |___publishers

   ​			  |___Tony		# publisher username

   ​				     |___24521		#task_id

   ​							|___dataset		#数据集

   ​								   |___0.jpg

   ​								   |___1.jpg

   ​									...

   ​                            |___submit		 #用户提交的文件

   ​								   |___102.csv		#work_id.csv

   ​								   |___123.csv

   ​							|___label.csv	  #通过审核后的成品文件

   ​					 |___96472

   ​              |___Lucy

   ​              |___Lily

   ​	   |___users

   ​			  |___张三			#user username

   ​					 |___33247.temp.csv		#work_id.temp.csv

   ​					 |___67493.temp.csv

   ​              |___李四

   ​              |___王二麻子

   

   三、更新记录

   1. 2020年8月9日  v0.1  luckyh6

   + 草稿初步完成，人要没了

   2. 2020年8月11日  v0.2  luckyh6

   + 细化了每个页面的信息
   + 对产品结构进行了修改
   + 明确了每个api的功能
   + 其他蓝图和路由还需要明确
   
   四、开发计划
   
   + 8月16日完成全部前端页面，并烧香祈祷没有bug
   + 8月17日完成前端逻辑js和向后端的访问请求，并烧香祈祷没有bug
   + 8月18日完成全部后端接口，并烧香祈祷没有bug
   + 8月19日整体调试，DEBUG
   + 8月20日进行测试，若成功则交付给甲方爸爸，不成功钱思远准备女装谢罪
   