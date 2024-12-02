from django.shortcuts import render
from django.http import HttpResponse


class Kitsch:
    def __init__(self, name):
        self.name = name

kitsch = [
    Kitsch('mission'),
    Kitsch('aboutme')
]

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def kitsch_index(request):
    return render(request, 'kitsch/index.html', {'kitsch' : kitsch})
