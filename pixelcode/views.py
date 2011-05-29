from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from django.template.loader import get_template

def index(request):
    context ={ 'nav' : Navigation.objects.get(slug='home') }
    return render_to_response ('index.html', context, context_instance = RequestContext(request))

def nav(request, nav):
    template = nav+'.html'    
    try:
        get_template(template)
    except:
        template = 'index.html'
    print template
    context ={ 'nav': Navigation.objects.get(slug=nav) }
    return render_to_response (template, context, context_instance = RequestContext(request))