from email import message

from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
import json
from fnmatch import translate
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _ 
from django.utils.translation import get_language,activate,gettext

# Create your views here.

def contact_view(request):
    trans=translate(language='fr')
    title=_("contact us")
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form=ContactForm(request.POST)
        data={}
        if form.is_valid():
            form.save()
            form=ContactForm()
           
            
            
            data['success']=True
            
            
            return HttpResponse(json.dumps(data),content_type='application/json')
        else:
            data['success']=False
            return HttpResponse(json.dumps(data),content_type='application/json') 
    else:
        form=ContactForm()
        template_name="contact/contact.html"
        context={"form":form,"title":title,"trans":trans}
        return render(request,template_name,context)

def translate(language):
    current_language=get_language()
    try:
        activate(language)
        text = gettext('contact us')
    finally:
        activate(current_language)
    return text
    
    
        
        
   
    

