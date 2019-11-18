#encoding:utf--8

from django import forms
from .contents import MessageType,SensitiveWordInit
import jieba

MESSAGE_TYPE_CHOICES = tuple([(i.value,i.value) for i in MessageType])

class MessageForm(forms.Form):
    content = forms.CharField(label='消息内容', max_length=100, required=True)
    message_type = forms.CharField(
        label='消息类型',
        max_length=10,
        widget=forms.Select(choices=MESSAGE_TYPE_CHOICES)
    )

    def clean_message_type(self):
        message_type = self.cleaned_data.get('message_type')

        if not message_type:
            raise forms.ValidationError('消息类型不能为空')
        try:
            message_type_obj = MessageType[message_type]
        except:
            raise forms.ValidationError('无效的消息类型')
        return message_type_obj

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if not content:
            raise forms.ValidationError("消息不能为空")

        cut_messge = jieba.lcut(content)
        print(cut_messge)

        check = list(set(cut_messge) & set(SensitiveWordInit))

        if check:
            raise forms.ValidationError("该消息涉及违禁词汇，已被屏蔽")

        return content
