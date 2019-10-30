# 什么是ORM 

全称 object relational mapping, 通过使用它，可以直接用python方法去使用数据库

通过**把表映射成类，把行作为实例，把字段作为属性**

## 优点

1. 使用简单
2. 性能好
3. 兼容好



# Django的ORM

1. 在`settings.py`中设置数据库信息（需提前在数据库中创建库）
2. 在应用app的models.py中以类的形式定义模型
3. 通过模型在目标数据库中创建对应的表
4. 在视图函数中通过对模型的操作实现目标数据可的读写操作

### Settings中数据库的配置



![image-20191028203654412](../Library/Application Support/typora-user-images/image-20191028203654412.png)



### Models层的书写

![image-20191028203801960](https://tva1.sinaimg.cn/large/006y8mN6ly1g8e72x3ps3j31g60o2thn.jpg)



## 同步数据库

![image-20191028203843568](https://tva1.sinaimg.cn/large/006y8mN6ly1g8e73lcvakj31ji0mqdnd.jpg)





## 字段方法所在位置

form django.db import models

models.CharField..

![image-20191030110104121](../Library/Application Support/typora-user-images/image-20191030110104121.png)



CharField 较短

TextField 长文本

![image-20191030110414031](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g1qetrubj31h00n4gsy.jpg)


![image-20191030110436228](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g1qslknjj31dw0kagr1.jpg)







![image-20191030110458288](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g1raj97oj31fk0u0wsm.jpg)

![image-20191030110608093](../Library/Application Support/typora-user-images/image-20191030110608093.png)

最后一个为 db_index



![image-20191030111022639](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g1wskktlj318g0t0qcn.jpg)

## 表关系

![image-20191030135222797](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g6llyacwj31ao0ieq60.jpg)



![image-20191030135244961](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g6lr1si4j31di0hs42k.jpg)

 ![image-20191030135602163](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g6p8v2dmj31cq0jqdjd.jpg)

在涉及到表关联是， on_delete要加上

## 联合索引

一个表中有两个字段要合并使用一个索引 

比如下面 
`unique_together=["day","hour"]`

`day=1 hour = 24`这样的值只能出现一次

### 联合索引的创建方法

![image-20191030140946760](https://tva1.sinaimg.cn/large/006y8mN6ly1g8g73jgpl2j31a80imjvs.jpg)

 





# 增删改查

## 增删改

增加方法

![image-20191030221102748](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gl0ih08dj31cy0t6tek.jpg)

![image-20191030221227888](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gl1pk2xvj31d40n00wr.jpg)



fff

![image-20191030221214704](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gl1mb01pj31a40kw0wu.jpg)

![image-20191030221323463](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gl2qculqj30yu0naaci.jpg)

