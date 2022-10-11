from django.shortcuts import render, redirect

from .models import Inbox
from .forms import InboxForm 

from django.contrib.auth.decorators import login_required

from django.db.models import Q

###### Esta seria la vista del el inbox
@login_required
def messages(request):
    
    user = request.user
    
    msg = Inbox.objects.filter(Q(reciever=user) | Q(sender=user)).order_by('-date')
    received = msg.filter(reciever=user).order_by('-date')
    sent = msg.filter(sender=user).order_by('-date')

    context =  {'title': 'Inbox',
                'user': user,
                'messages': msg,
                'received': received,
                'sent':sent,
                }
    return render(request, 'messages.html', context)

###### Esta es la vista para crear un nuevo mensaje
@login_required
def new_message(request):

    if request.method != 'POST':
        form = InboxForm()
    
    else:
        form = InboxForm(data=request.POST)

        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messages')
    
    context = {'form': form, 'title': 'New message'}
    return render(request, 'newMessage.html', context)

###### Vista para eliminar un mensaje
@login_required
def delete_msg(request, msg_id):

    #se intenta bucar el mensaje por id
    try:
        msg = Inbox.objects.get(id=msg_id)
        msg.delete()
        return redirect('messages')
    # Si levanta una excepcion renderiza a la pagina de inicio
    except Exception as exc:
        return redirect('inicio.html')

