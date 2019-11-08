#coding:utf-8
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class User(models.Model):
    username = models.CharField(unique=True, max_length =50, blank=False)
    age = models.SmallIntegerField(default=0)
    phone = models.IntegerField(db_index=True, default=0, blank=True)
    email = models.EmailField(blank=True)
    info = models.TextField()
    create_time  = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = ['username', 'phone']

    def __str__(self):
        return 'User{}'.format(self.username)

class Userprofile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    birthday = models.CharField(max_length=100, blank=True, default ='')

    def __str__(self):
        return 'User{}, birthday{}'.format(self.user.username, self.birthday)

class Diary(models.Model):
    user = models.ForeignKey(User, related_name='diary', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()
    create_time  = models.IntegerField()

class Group(models.Model):
    uesr = models.ManyToManyField(User, related_name='group')
    name = models.CharField(max_length=20)
    create_time = models.IntegerField()