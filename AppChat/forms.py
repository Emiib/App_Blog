from django import forms

from .models import Inbox

class InboxForm(forms.ModelForm): 
    class Meta:
        model = Inbox
        fields = ['reciever','msg']
        widgets = {'msg': forms.Textarea(attrs={'cols': 80})}  #Widget para agrandar el area de texto a 80 columnas