from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from django.template.loader import get_template
from django.utils import simplejson
from forms import *

def index(request):
    context = {'nav' : Navigation.objects.get(slug='home')}
    return render_to_response('index.html', context, context_instance = RequestContext(request))

def nav(request, nav):
    template = nav+'.html'    
    try:
        get_template(template)
    except:
        template = 'index.html'
    print template
    context ={ 'nav': Navigation.objects.get(slug=nav) }
    return render_to_response (template, context, context_instance = RequestContext(request))

def subnav(request, nav, subnav):
    template = nav+'.html'    
    try:
        get_template(template)
    except:
        template = 'index.html'
    print template
    context ={ 'nav': Navigation.objects.get(slug=nav), 'subnav' : SubNavigation.objects.get(slug=subnav) }
    return render_to_response (template, context, context_instance = RequestContext(request))

def subsubnav(request, nav, subnav, subsubnav):
    template = nav+'.html'    
    try:
        get_template(template)
    except:
        template = 'index.html'
    print template
    context ={ 'nav': Navigation.objects.get(slug=nav), 'subnav' : SubNavigation.objects.get(slug=subnav), 'subsubnav' : SubSubNavigation.objects.get(slug=subsubnav) }
    return render_to_response (template, context, context_instance = RequestContext(request))


def contact_form(request):
    comment = request.POST.get('comment', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')
    if comment == 'Comments':
        comment = ''
    if name == 'Name':
        name = ''
    if email == 'Email Address':
        email = ''
    if comment and email and name:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            a = form.save()
            to_return = {'message' : 'Thanks for contacting us. We should get back to you shortly.', 'success' : True }
        else:
            print form.errors
            to_return = {'message' : 'Please enter a valid email address.', 'success' : False }
    else:
        to_return = {'message' : 'Some of the required fields are missing.', 'success' : False }    
    return HttpResponse(simplejson.dumps(to_return), mimetype='application/json')    