from django.shortcuts import render
import os

def home(request):
    return render(request, 'myapp/home.html')

def exe_open(request):
    present_path = os.getcwd()
    path_list = present_path.split(os.path.sep)
    exe_path = os.path.join(os.path.abspath('mouse-cursor-control'), 'mouse-cursor-control.exe')
    os.popen(exe_path)
    return render(request, 'myapp/home.html')

def exe_close(request):
    present_path = os.getcwd()
    path_list = present_path.split(os.path.sep)
    exe_path = os.path.join(os.path.abspath('mouse-cursor-control'), 'mouse-cursor-control.exe')
    os.system('taskkill /f /im mouse-cursor-control.exe')
    return render(request, 'myapp/home.html')

