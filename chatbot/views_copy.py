from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from my_sql_connect import database_fetch 
from chat.models import Chat


def home(request):
    chats = Chat.objects.all()
    ctx = {
        'home': 'active',
        'chat': chats
    }
    print("tried = " ,database_fetch("SELECT * FROM CUSTOMERS"))
    if request.user.is_authenticated:
        return render(request, 'chat.html', ctx)
    else:
        return render(request, 'base.html', None)


def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(user=request.user, message=msg)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg, 'user': chat_message.user.username})
    else:
        return HttpResponse('Request must be POST.')


def messages(request):
    chat = Chat.objects.all()
    return render(request, 'messages.html', {'chat': chat})
