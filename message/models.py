from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Message(models.Model):
    send_by = models.ForeignKey(User,on_delete = models.CASCADE)
    content = models.TextField(max_length=200)
    time_send=models.DateTimeField(auto_now_add=True)
    send_to = models.CharField(max_length=20)

    # def get_absolute_url(self):
    #     return reverse('messages:create-message', args=[self.pk])
