from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
#from django.template import RequestContext, loader


# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home/index.html')
