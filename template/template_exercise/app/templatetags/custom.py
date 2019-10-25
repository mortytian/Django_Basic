# coding:utf-8

from django import template
from app.contents import SensitiveWord
import jieba


register = template.Library()


@register.filter(name='deep_check_message')
def deep_check(value):
    cut_message = jieba.lcut(value)
    new_message = []
    for m in cut_message:
        if m in SensitiveWord:
            new_message.append('*')
        else:
            new_message.append(m)

    if new_message:
        return ''.join(new_message)
    return new_message



@register.filter
def sample_check(value):
    cut_message = jieba.lcut(value)
    print(cut_message)
    check = list(set(cut_message) & set(SensitiveWord))
    print(SensitiveWord)
    if len(check) != 0 :
        return '该消息涉及违禁词汇， 已被屏蔽'
    return value

@register.filter
def add_year(value, args):
    return '{}{}'.format(value,args)