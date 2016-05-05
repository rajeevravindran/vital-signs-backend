from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from random import randint
from .models import HeartBeat
import json
#import serial

#ser=serial.Serial('COM3',38400)
temp=5

passed=130;
time=timezone.now()


# Create your views here.
def index(request):
    data=HeartBeat.objects.all()
    context={'current_bpm':data}
    return render(request, 'heartbeat/index2.html',context)

def update(request):
    #temp=int(ser.readline())
    temp=randint(68,100)
    print ("UPDATED")
    data=HeartBeat(current_bpm=temp,current_time=timezone.now())
    data.save()
    return_reponse={'current_heartbeat':temp,'current_time':str(timezone.now())}
    print return_reponse
    return HttpResponse(json.dumps(return_reponse))
