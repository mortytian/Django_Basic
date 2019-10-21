创建新项目：django-admin startproject  xxx

创建应用: python manage.py startaoo app

启动：python manage.py runserve

​			PYTHONENCODING=utf-8 python manage,py runserve 可以指定编码

![image-20191021232110917](/Users/typeme/Library/Application Support/typora-user-images/image-20191021232110917.png)



url中的参数

两种传参数的方式，对应代码中两种不同的写法

1. 在url后面用？开始，键与值用等号连接，每对键值用`&`号区分，如：

   http://127.0.0.1:8800/app?name=tian&age=30

   视图读取参数的方法：

   request.GET.get(参数名)，如：

   name = request.GET.get('name', '') 

   最后为默认值，不传值以默认值为准

   urls.py中写：

   path('',index)

2. 在路由的参数中用`/`分隔符分开，如:

   http://127.0.0.1:8800/app/tian/30

   视图读取参数的方法：

   def index(request, name,age):

   ​	print(参数名)

   urls.py中写:

   Path('\<str:name>/\<int:age>', index)

即第1种方法通过request的方法获得参数 urls中不需要特别设置

第2中方法通过 urls中获得参数 不用request方法

![image-20191021231028539](https://tva1.sinaimg.cn/large/006y8mN6ly1g8685b2oxwj31hu0u0tla.jpg)

![image-20191021232837235](https://tva1.sinaimg.cn/large/006y8mN6ly1g868ocj324j31i00riwlv.jpg)



## 视图

分为三部分：

1. 用户的请求 request

   ![image-20191021234004575](https://tva1.sinaimg.cn/large/006y8mN6ly1g8690i8pjij31ak0o8dla.jpg)

   ![image-20191021234101017](https://tva1.sinaimg.cn/large/006y8mN6ly1g86911si4rj31b20t2gui.jpg)



![image-20191021234121897](https://tva1.sinaimg.cn/large/006y8mN6ly1g8691ga0uwj31ho0tqqf9.jpg)





2. 对用户请求对逻辑处理 handler

3. 将处理后的数据返回给用户 response

![image-20191021234200560](https://tva1.sinaimg.cn/large/006y8mN6ly1g869250vy3j319a0se12l.jpg)

### 视图面向对象的写法

```python
from django.views.generic import View
Class Test(View):
  def get(self,request):
    return xxx
```

