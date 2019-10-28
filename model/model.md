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



