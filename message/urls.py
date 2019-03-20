from django.urls import path
from .views import *

app_name = 'messages'

urlpatterns = [
    path('send_message/<int:receiver>/', CreateMessageView.as_view(), name='create-message'),
]
