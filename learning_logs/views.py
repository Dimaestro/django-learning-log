from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ''' Домашня страница Learning_Log '''
    return render(request, 'learning_logs/index.html')