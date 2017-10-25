# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import MySQLdb

from .models import UserMessage
# Create your views here.



def messageindex(request):

    # all_messages = UserMessage.objects.filter(name='zgl')
    # for message in all_messages:
    #     print message.name
    if request.method == "post":
        name = request.POST.get('name','')
        message = request.POST.get('message')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        user_message = UserMessage
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'asdfsa1'
        user_message.save()

    return render(request, 'message_index.html')