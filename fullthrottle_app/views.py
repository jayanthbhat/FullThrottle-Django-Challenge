from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.management import call_command

def home(request):
    return render(request,'home.html')

def command_upload(request):
    if request.method == "POST":
        username = request.POST['username']
        response=call_command('throttle_command',username)       
        return render(request,'success.html',context={'username':username})

    return render(request,'custom_management_cmd.html')