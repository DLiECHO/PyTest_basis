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

# 用户账户

## 让用户能够输入数据

### 添加新主题

创建一个让普通用户也能添加新主题的页面

**首先建立一个让用户能够输入信息的表单：`from django import forms`**

```python
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
```

该表单中的`class Meta`为内嵌类，[[Django中的class Meta - Yang-hao - 博qu客园 (cnblogs.com)](https://www.cnblogs.com/yang220/p/10749339.html)]

**再定义URL模式**：**`new_topic`**

**再写视图函数**

*区别GET和POST请求，其中当用户填写好一个表单并提交时，用户的浏览器将会发送POST请求*

**最后再写模板**，对于本页面还需要

### 添加新条目

创建用于添加新条目的表单->定义URL->编写视图(区分GET和POST请求，注意将新增entry关联到topic再提交数据库)->编写模板

### 编辑条目

定义URL模式->编写视图->编写模板->将编辑条目的页面连接到查看每个主题详情中每个条目的下方

## 创建用户账户

创建一个用户注册和身份验证系统，将另外创建一个架构与`learning_logs`相似的应用程序

### 应用程序users

通过`startapp`新建应用程序`users`

将刚刚新建的程序添加到`learning_log/settings.py`中，以此来将应用程序`users`包括到项目中

将其URL包括到`learning_log/url.py`

### 登录页面

在`learning_log/users/`中新建`urls.py`，定义登录页面URL->编写模板`login.html`，**继承应用程序`learning_logs`中的模板`base.html`，即一个应用程序中的模板可以继承另一个应用程序中的模板**->在`base.html`中添加到此登录页面的链接，以此来让所有页面都包含他

### 注销

定义注销URL->编写视图，调用视图函数`logout_view()`在`base.html`中添加链接到注销视图的标签

### 注册页面

定义URL->视图，`UserCreationForm`创建表单->模板->链接到`base.html`

## 让用户拥有自己的数据

### 使用`@login_required`限制访问

对于某些页面，应该只允许已登录的用户来访问他们，装饰器`@login_required`可以做到，装饰器是放在函数定义之前的指令

1.只允许已登录的用户请求`topics`页面

2.全面限制

### 将数据关联到用户

只需要将高层的数据关联到用户，底层的会自动关联，比如将主题关联到用户，因为所有条目都与特定主题相关联，只要每个主题都归属于特定用户，那么所有条目就都有各自所有者。

1.修改模型, 添加外键

2.确定当前有哪些用户

3.迁移数据库

### 只允许用户访问自己的主题

`topics = Topic.objects.filter(owner=request.user).order_by('date_added')`

### 保护用户的主题、页面`edit_entry`、`new_entry`

通过比对请求者和主题所属者来确定是否返回404页面

将新主题关联到当前用户

```python
new_topic =  form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
```

# 设置应用程序样式并对其进行部署
