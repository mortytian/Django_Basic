from django.db import models
from .contents import MessageType
# Create your models here.
class Message(models.Model):
    content = models.TextField()
    message_type = models.CharField(max_length=10, db_index=True)
    create_time = models.IntegerField(default=0)

    def __str__(self):
        return 'type:{},content{}'.format(self.message_type, self.content)

    def get_message_type(self):
        try:
            return MessageType[self.message_type]
        except:
            return MessageType['info']