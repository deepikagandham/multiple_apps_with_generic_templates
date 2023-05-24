from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_string(request):
    return HttpResponse('This is app_string Response')


def app_htmlpage(request):
    return render(request,'app_htmlpage.html')