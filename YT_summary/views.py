from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
from django.shortcuts import loader
from django.shortcuts import render
import json
import sys
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
from django.views.generic import TemplateView
from subprocess import run,PIPE

#format with nltk(FINAL)
def srch(request):
    return render(request,'srchbx.html')

def get_sum(request):
    inpt= request.POST.get('get_url')
    outpt= run([sys.executable,'D://code//project Env//YT_summary//summurize_byId.py',inpt],shell=False,stdout=PIPE)
    print(outpt)
    return render(request,'srchbx.html',{'data1':outpt.stdout.decode('utf-8',errors="ignore")})


        


