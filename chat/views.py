from django.shortcuts import render

from .models import Message

def home(request):
    return render(request, 'home.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:15]

    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages})