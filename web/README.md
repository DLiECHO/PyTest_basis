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

管理员在后台操作，可添加”主题，暂时理解：*定义的模型（类）的实例化*

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

## 设置样式

### 应用程序django-bootstrap4

使用**django-bootstrap4**来将Bootstrap继承到项目中，首先安装

`pip install django-bootstrap4`，似乎已经默认安装了

修改`setting.py`，添加应用程序bootstrap4，并添加设置，允许其使用jQuery

### 修改base.html

修改后格式与一般HTML文件一致，注意在head中要包括两个标签：`{% bootstrap_css %}`、`{% bootstrap_javascript %}`
这两个标签让Django包含所有的Bootstrap样式文件。

### 使用jumbotron设置主页样式

### 设置登录界面样式

注意这里已经不需要`{if form.errors}`代码块，因为`django-bootstrap4`会自动管理表单错误。

### 设置注册界面样式

### 设置new_topic、topics、topic中条目页面样式

可以参考Bootstrap官方文档，相关博客

> https://blog.csdn.net/qq_19268039/article/details/83272949?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164197403316781685387672%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164197403316781685387672&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-83272949.first_rank_v2_pc_rank_v29&utm_term=django+%E5%AF%BC%E8%88%AA%E6%A0%8F%E8%87%AA%E9%80%82%E5%BA%94&spm=1018.2226.3001.4187

## 更改网站的logo：Favicon
制作ico->置于静态文件目录->`href`引用

## 在centos上部署项目：Nginx+uWSGI+Django
*由于个人时间关系，部署步骤暂时就不详细描述，几个关键步骤如下：*
1.移植项目至centos；
2.为centos配置环境，包括下载对应版本python，安装nginx（通过wget下载，后续自定义安装，注意centos8更改环境变量有新的更安全的方法）；
3.重新创建虚拟环境，并在虚拟环境内安装对应版本的Bootstrap4、uwsgi
4.确保项目能通过`python manage.py runserver 0.0.0.0:8000`命令启动，并能通过互联网访问；
5.配置uwsgi，编写`myuwsgi.ini`文件，确保项目能通过uwsgi启动并可以被访问，这里注意uwsgi默认不支撑加载静态文件；
```
# mysite_uwsgi.ini file
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /.../name
# Django's wsgi file（在项目中时默认存在wsgi.py文件的，这里也就是去项目里寻找wsgi文件）
module          = name.wsgi
# the virtualenv (full path)
home            = /.../.../虚拟环境文件夹

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 1
enable-threads  = true
threads         = 2
# the socket (use the full path to be safe)（与Nginx的通信方式参数，详见步骤7）
socket          = /.../.../name.sock
# socket          = 0.0.0.0:9001
# http = 0.0.0.0:9001
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
# daemonize uwsgi and write messages into given log
daemonize       = /.../.../myuwsgi.log
```
6.在项目中的`setting.py`文件中增加关于`static_root`的描述，如`STATIC_ROOT = BASE_DIR/'static'`,也就是在项目根目录下新建`static`目录（目前由于本人提前手动mkdir了，所以不得知是否需要手动建立目录）,再通过`python manage.py collectstatic`命令，copy项目中的静态文件至该目录下，另外注意将`setting.py`中的`DEBUG`参数改为`False`；
7.上述就是说，在生产环境中，不建议通过Django去提供静态文件，建议通过Nginx完成此任务，这里也就是要配置Nginx去提供静态文件，实现方法是**通过Nginx的反向代理功能将动态请求转发给uwsgi，自己处理静态请求，这里也是完成了动静分离的架构**。
具体来说是主要在Nginx的配置文件`nginx.conf`中修改虚拟主机部分配置，即修改server标签内容：包括建立upstream池，在池中标明Nginx反向代理的对象，或者说标明与反向代理对象（uwsgi）的进程通信方式，建议**用socket文件进行管道通信**，比端口通信更加稳定安全；还有添加`location /static{...}`以达成处理静态文件的能力，该标签意味着当有请求为`diary.dliecho.top/static/XXX.XXX`此类url时，给他返回标签内定义的内容，而此时通过alia命令，在请求过程中引入**6**中定义的新的static文件目录，以此来让nginx直接提供静态请求；最后还有基础的`location / {...}`标签，变迁中通过`uwsgi_pass`属性指明upstream，同时需要include一个文件(在nginx的conf文件夹中默认存在)：`uwsgi_params`，该文件似乎是表面Nginx将动态请求转发给uwsgi时，所转发的内容的格式；以下为`nginx.conf`部分示例内容：
```
upstream stream {
        server unix:///.../.../name.sock;
        # server 127.0.0.1:9001;
    }

    server {
        listen       80;
        server_name  diary.dliecho.top;
        client_max_body_size 16m;
        location / {
            uwsgi_pass stream;
            include uwsgi_params;
        }

        location /static {
            alias /.../.../static;
        }

        error_page  404              /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
```
8.最后在虚拟环境里面通过`uwsgi --ini myuwsgi.ini`启动uwsgi服务，再通过`nginx`或`nginx -s reload`启动nginx，完成项目的部署。

***Notice***
*时间仓促，水平有限，上述仅为部分步骤，且或许并不十分正确！*