from django.urls import path
from .views import *

urlpatterns = [
    
    path('messages/', messages, name="messages"),
    path('new_message/', new_message, name="new_message"),
    path('delete_msg/<msg_id>', delete_msg, name="delete_msg"),

    ]