from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
import json
import os
from django.conf import settings

# Portfolio Homepage
def home(request):
    return render(request, 'portfolio/home.html')

# Skills JSON file
def skillsData(request):
    path = os.path.join(settings.BASE_DIR, "portfolio\static\portfolio\data\skills.json")
    with open(path , 'r') as myfile:
        data=myfile.read()
    response = HttpResponse(content=data)
    response['Content-Type'] = 'application/json'
    return response