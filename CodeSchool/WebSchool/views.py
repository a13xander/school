from django.shortcuts import render_to_response
from django.template.context import RequestContext

def login(request):
    if request.method == 'POST':
        return render_to_response('welcome_administrator.html', context_instance = RequestContext(request))
    else: 
        return render_to_response('login.html', context_instance = RequestContext(request))
    
def base_administrator(request):
    return render_to_response('base_administrator.html',{'base_administrator':base_administrator}, context_instance=RequestContext(request))

def qualification(request):
    return render_to_response('qualification.html',{'qualification':qualification}, context_instance=RequestContext(request))
