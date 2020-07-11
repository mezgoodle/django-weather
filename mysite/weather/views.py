from django.shortcuts import render

def index(request):
    template_name = 'index'
    return render(request, template_name)
