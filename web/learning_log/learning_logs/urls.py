"""定义learning_logs的URL模式"""

from django.urls import include, path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 主题列表界面
    path('topics', views.topics, name='topics'),
    # 特定主题界面
    path('topics/<int:topic_id>', views.topic, name='topic')
]
