# 变量作用域
&emsp;&emsp;**作用域指的是变量的有效范围。** 变量并不是在哪个位置都可以访问的，访问权限取决于这个变量是在哪里赋值的，也就是在哪个作用域内的。  
&emsp;&emsp;通常而言，在编程语言中，变量的作用域从代码结构形式来看，有块级、函数、类、模块、包等由小到大的级别。但是在Python中，没有块级作用域，**也就是类似if语句块、for语句块、with上下文管理器等等是不存在作用域概念的，他们等同于普通的语句。**  
```python
if True:            # if语句块没有作用域
    x = 1
print(x)
# 1
def func():         # 函数有作用域
    a = 8
print(a)
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     a
# NameError: name 'a' is not defined
```  
  
  
  
  参考博客：<https://www.cnblogs.com/Jolly-hu/p/12228320.html>