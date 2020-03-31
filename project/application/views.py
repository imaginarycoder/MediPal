from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from application import scripts
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTERNAL_DIR = os.path.join(BASE_DIR, 'external_files')

#from application.models import Subscribers
from application.forms import NewSubscriberForm
# Create your views here.

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
#    return render(request, 'application/gait.html')
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
"""
    subscribers_list = Subscribers.objects.order_by('email')
    subscribers_dict = {'subscribers':subscribers_list}
    return render(request, 'application/see_subscribers.html', context = subscribers_dict)
"""

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
        #image_processed = run([sys.executable, 'C:\\Minor\\Minor_django\\image_processing.py', str(fileurl), str(filename)], shell=False, stdout=PIPE)
        image_predict = run([sys.executable, os.path.join(EXTERNAL_DIR,'predict_spiral.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE) #A cloud path can be given later for this external file
        if(b"Patient" in image_predict.stdout):
            result = "Patient"
        elif(b"Healthy" in image_predict.stdout):
            result = "Healthy"
        else:
            result = "Sorry, no value"
        my_dict = {'raw_url':templateurl, 'result':result}
        #print(image_processed.stdout)
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
        #image_processed = run([sys.executable, 'C:\\Minor\\Minor_django\\image_processing.py', str(fileurl), str(filename)], shell=False, stdout=PIPE)
        image_predict = run([sys.executable, os.path.join(EXTERNAL_DIR, 'predict_meander.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE) #A cloud path can be given later for this external file
        if(b"Patient" in image_predict.stdout):
            result = "Patient"
        elif(b"Healthy" in image_predict.stdout):
            result = "Healthy"
        else:
            result = "Sorry, no value"
        my_dict = {'raw_url':templateurl, 'result':result}
        #print(image_processed.stdout)
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
        #image_processed = run([sys.executable, 'C:\\Minor\\Minor_django\\image_processing.py', str(fileurl), str(filename)], shell=False, stdout=PIPE)
        image_predict = run([sys.executable, os.path.join( EXTERNAL_DIR ,'predict_circle.py'), str(fileurl), str(filename)], shell=False, stdout=PIPE) #A cloud path can be given later for this external file
        if(b"Patient" in image_predict.stdout):
            result = "Patient"
        elif(b"Healthy" in image_predict.stdout):
            result = "Healthy"
        else:
            result = "Sorry, no value"
        my_dict = {'raw_url':templateurl, 'result':result}
        #print(image_processed.stdout)
        return render(request, 'application/result.html', context = my_dict) 


"""  
def upload_meander(request):
    #inp = request.FILES['file']
    #model = run([sys.executable, 'D:\\SUBJECTS FOLDER\\Minor\\Datasets\\Healthy and Patient\\outputs\\predict_1.py', inp], shell = False, stout = PIPE)
    #latest_array = run([sys.executable, 'D:\\SUBJECTS FOLDER\\Minor\\Datasets\\Healthy and Patient\\outputs\\predict_2.py', inp], shell = False, stout = PIPE)
    LABELS = ['Healthy', 'Patient']
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            model = scripts.openFile()
            prediction = LABELS[model.predict(scripts.prepare(request.FILES['file']))[0]]
            return HttpResponseRedirect(request, 'application/result.html', {'key':prediction})

    else:
        #form = UploadFileForm()
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            model = scripts.openFile()
            prediction = LABELS[model.predict(scripts.prepare(request.FILES['file']))[0]]
            return HttpResponseRedirect(request, 'application/result.html', {'key':prediction})
    return render(request, 'application/result.html', {'key':prediction})


def upload_meander(request):
    LABELS = ['Healthy', 'Patient']
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(request, 'application/meander.html')
    else:
        form = UploadFileForm()
    model = scripts.openFile()
    prediction = LABELS[model.predict(scripts.prepare(request.FILES['file']))[0]]

def upload_meander(request):
    if request.method == 'POST':
        LABELS = ['Healthy', 'Patient']
        f = request.files['file']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, '.\\meander_uploads', secure_filename(f.filename))
        f.save(file_path)
        
        model = scripts.openFile()
        prediction = LABELS[model.predict(scripts.prepare('Test_3.jpg'))[0]]
        dictionary = {'key':prediction}
        return render(request, 'application/meander.html', content = dictionary)

def upload_spiral(request):
    if request.method == 'POST':
        LABELS = ['Healthy', 'Patient']
        f = request.files['file']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, '.\\spiral_uploads', secure_filename(f.filename))
        f.save(file_path)
        
        model = scripts.openFile()
        prediction = LABELS[model.predict(scripts.prepare('Test_3.jpg'))[0]]
        dictionary = {'key':prediction}
        return render(request, 'application/spiral.html', content = dictionary)
"""