from django.shortcuts import render
from .form import *
# Create your views here.
def createObject(request):
    if request.method == 'POST':
form=


    return render(request, 'inspectionForm/createObject.html')