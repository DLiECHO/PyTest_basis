# Django入门

## 建立项目

### 制定规范

建一个名字叫**学习笔记**的web应用程序

### 建立虚拟环境

`python -m venv NAME`

### 激活虚拟环境

`Win: NAME\Scripts\activate`

`Linux:source NAME/bin/activate`

### 停止虚拟环境

`deactivate`

### 安装Django

`pip install Django`

### 在Django中创建项目

新建一个名为`learning_log`的项目

### 创建数据库

`python manage.py migrate`

### 查看项目

`python manage.py runserver`

## 创建应用程序

`python manage.py startapp learning_logs`

### 定义模型

修改创建的应用程序`learning_logs`中的`models.py`

### 激活模型

1. 首先需要让**Django**将应用程序包含到之前创建的项目`learning_log`中，即打开项目目录中`settings.py`，修改`INSTALLED APPS`列表——增加我们刚刚创建并修改的的应用程序`learning_logs`字段。
2. 然后需要让**Django**修改数据库，使其能够存储与在应用程序中定义的新模型相关联的数据。
   * 修改数据库：`python manage.py makemigrations learning_logs`;
   * 应用该迁移（修改）：`python manage.py migrate`

*每当需要修改**学习笔记**（项目）管理的数据时，都采取如下三个步骤：**修改`models.py`**；**对`learning_logs`调用`makemigrations`**；**让Django迁移项目**。*

### Django管理网站

#### 创建超级用户

`python manage.py createsuperuser`

#### 向管理网站注册模型

修改`admin.py`

#### 添加主题

暂时理解：*定义的模型（类）的实例化*

### 定义模型Entry

上一节中我们添加了两个主题：国际象棋和攀岩知识，那么作为*学习笔记*，我们自然需要为这两个学习主题做一些笔记，于是我们需要再定义新模型：**Entry**（条目）。

新模型有这样的特点：**多对一**，一个主题（例：象棋）可以有多个记录**条目**。

### 迁移模型Entry

### 向管理网站注册Entry

### Django shell

`python manage.py shell`

`ctrl+z`后*回车*来退出InteractiveConsole

## 创建网页：学习笔记主页

### 影射URL

寻找一个与客户请求所匹配的URL，并向视图索求一个与该URL相匹配的结果

参考资料：[https://zhuanlan.zhihu.com/p/348392647](https://zhuanlan.zhihu.com/p/348392647)

### 编写视图

视图：为映射URL所做的工作递上一个合适的结果，如html页面。

### 编写模板（HTML）

如编写主页`index.html`

## 创建其他网页

### 模板继承

创建父模板`base，html`，更改`index.html`，使其继承`base，html`，为`base，html`的子模版。

### 显示所有主题（topics）的界面

定义**URL模式**->编写**视图**->编写**模板**

### 显示特定主题的页面

定义**URL模式**->编写**视图**->编写**模板**

*因为topic的URL模式需要提供实参`topic_id`，所以在`topics.html`里添加可以跳转至`topic.html`的超链接时，其中的模板标签url需要添加属性`topic.id`，具体如下：*

`<a href="{% url 'learning_logs:topic' topic.id%}">{{ topic }}</a>`
