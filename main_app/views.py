from django.shortcuts import render
from django.http import HttpResponse


class Kits:
    def __init__(self, name):
        self.name = name,

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def kitsch_index(request):
    return render(request, 'kitsch/index.html', {'kitsch' : kitsch})
