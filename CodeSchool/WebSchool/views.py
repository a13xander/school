from django.shortcuts import render_to_response
from django.template.context import RequestContext

def login(request):
    if request.method == 'POST':
        return render_to_response('welcome_administrator.html', context_instance = RequestContext(request))
    else: 
        return render_to_response('login.html', context_instance = RequestContext(request))