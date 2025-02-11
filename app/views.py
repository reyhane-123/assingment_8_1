from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

list1=[
    {"id":1,"name":"class_python"},
    {"id":2,"name":"class_html"},
    {"id":3,"name":"class_jango"},
    {"id":4,"name":"class_c#"}
]

def detail(request):
    context={'show':list1}
    return render(request,'app/list.html',context=context)
