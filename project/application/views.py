from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTERNAL_DIR = os.path.join(BASE_DIR, 'external_files')

from application.forms import NewSubscriberForm

def index(request):
    return render(request, 'application/index.html')

def aboutPage(request):
    return render(request, 'application/aboutPage.html')

def contactPage(request):
    return render(request, 'application/contactPage.html')

def diagnosis(request):
    return render(request, 'application/diagnosis.html')

def doctors(request):
    return render(request, 'application/doctors.html')

def meander(request):
    return render(request, 'application/meander.html')

def spiral(request):
    return render(request, 'application/spiral.html')

def circle(request):
    return render(request, 'application/circle.html')

def gait(request):
    # return render(request, 'application/gait.html')
    run([sys.executable, os.path.join(EXTERNAL_DIR,'webcamGait.py')], shell=False, stdout=PIPE)
    return render(request, 'application/gait.html')

def subscribers(request):

    form = NewSubscriberForm()

    if request.method == "POST":
        form = NewSubscriberForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR: FORM INVALID')
    form_dict = {'form':form}
    return render(request, 'application/subscribers.html', context = form_dict)

def upload_spiral(request):
    if request.method == "POST":
        image = request.FILES['image']
        print('image is: ', image)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        fileurl = fs.open(filename)
        templateurl = fs.url(filename)
        print('File raw url: ',filename)
        print('File full url: ', fileurl)
        print('Template url: ', templateurl)
        image_predict = run([sys.executable, os.path.join( EXTERNAL_DIR ,'predict_spiral.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE)
        result = image_predict.stdout.decode()
        print(result)
        my_dict = {'raw_url':templateurl, 'result':result}
        return render(request, 'application/result.html', context = my_dict)

def upload_meander(request):
    if request.method == "POST":
        image = request.FILES['image']
        print('image is: ', image)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        fileurl = fs.open(filename)
        templateurl = fs.url(filename)
        print('File raw url: ',filename)
        print('File full url: ', fileurl)
        print('Template url: ', templateurl)
        image_predict = run([sys.executable, os.path.join( EXTERNAL_DIR ,'predict_meander.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE)
        result = image_predict.stdout.decode()
        print(result)
        my_dict = {'raw_url':templateurl, 'result':result}
        return render(request, 'application/result.html', context = my_dict)

def upload_circle(request):
    if request.method == "POST":
        image = request.FILES['image']
        print('image is: ', image)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        fileurl = fs.open(filename)
        templateurl = fs.url(filename)
        print('File raw url: ',filename)
        print('File full url: ', fileurl)
        print('Template url: ', templateurl)
        image_predict = run([sys.executable, os.path.join( EXTERNAL_DIR ,'predict_circle.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE)
        result = image_predict.stdout.decode()
        print(result)
        my_dict = {'raw_url':templateurl, 'result':result}
        return render(request, 'application/result.html', context = my_dict)