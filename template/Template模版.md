# Template 模版

模版可以动态生成Html网页，它包括部分Html代码和 一些特殊语法



## Template 配置方法

Template模版存放在 templates 目录中

通过在项目Settings的templates的DIRS列表中添加对应的路径即可，如:

**os.path.join(BASE_DIR, 'templates')**



## Template与视图的绑定

在view中完成通过**from django.shortcues import render** 模块

**return render(request, template_path, {k:v})** 字典中的key和value就是要向前端渲染出的数据



## Template展示渲染的数据

在html中以{{}}为标示，在双大括号中传入视图中传入的数据



# Template内置标签与静态文件配置

## 变量与标签

变量用**{{}}**双大括号包裹 比如我们后端渲染过来的数据，用双大括号包裹，如: {{name}}

内置标签类型：用{% %}大括号 左右各一个百分号包裹

![image-20191024223724532](https://tva1.sinaimg.cn/large/006y8mN6ly1g89o1yq6vlj318i0rsk2g.jpg)



![image-20191024224028246](https://tva1.sinaimg.cn/large/006y8mN6ly1g89o53au9wj319o0qutma.jpg)



## 静态文件配置

项目根目录创建 ‘static‘ 与 ’template' 文件夹同级

STATICFILES_DIRS  = (os.path.join(BASE_DIR, 'static'),)



## 静态文件类型

Css 样式文件

Javascript文件

image 图片文件等







# 模版内置过滤器

## 过滤器的作用

用于在html模版中，对于渲染过来的数据进行二次操作使用，过滤器就是用来处理这些数据的模版引擎中使用的函数。

**分隔符之间不要有空格，否则报错**



![image-20191025000645287](https://tva1.sinaimg.cn/large/006y8mN6ly1g89qmv8eknj31be0t6ao2.jpg)



![image-20191025000905815](https://tva1.sinaimg.cn/large/006y8mN6ly1g89qpmnwmaj31500rewpo.jpg)





![image-20191025001232097](https://tva1.sinaimg.cn/large/006y8mN6ly1g89qswk80sj318w0qe7g3.jpg)



## 自定义过滤器

在Django服务器端编写函数，在模版中可以直接调用的过滤器函数



### 定义自定义函数规则

在应用下创建 **templatetags** 文件夹

在文件夹下创建 **myfilter.py**

```python
from django import template
register = template.Library() # 定义过滤器
@register.fliter
def test_filter(value, args):
	return value + args

{% load myfilter %}
{{data | test_filter : 3}}
```





# 其他模版引擎

## Jinja2

Jinja2是一套模仿Django模版的模版引擎，有Flask开发者开发，它的使用场景和Django的模版非常相似。它速度快，被广泛使用。

Jinja2提倡让Html设计者和后端Python开发工作分离

https://palletsprojects.com/p/jinja/

![image-20191025103204659](https://tva1.sinaimg.cn/large/006y8mN6ly1g8a8pfcto3j30uw0s0dp0.jpg)



## Mako

mako模版算是python里面比较出色的一个模版，它宣称有比jinjia2更快的解析速度以及更多的语法支持

最大的特点在于，它可以允许你在Html中随意书写python代码