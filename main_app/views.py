from django.shortcuts import render


class Mission:
    def __init__(self, name):
        self.name = name

mission = [
    Mission('mission1'),
    Mission('aboutme')
]

class Love:
    def __init__(self, name, phone_number, email):
        self.name = name,
        self.phone_number = phone_number,
        self.email = email,

love = [
    Love('Mikey', '5555555555', 'blahblah@blah.com'),
    Love('Joseph', '9999999999', 'mablah@blah.com')
]

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mission_index(request):
    return render(request, 'kitsch/index.html', {'mission' : mission})

def love(request):
    return render(request, 'kitsch/love.html', {'love' : love})

def contact(request):
    return render(request, 'kitsch/contact.html', {'contact' : contact})

def blog(request):
    return render(request, 'kitsch/blog.html', {'blog' : blog})

def anita(request):
    return render(request, 'blogs/anita.html', {'anita' : anita})

def deena(request):
    return render(request, 'blogs/deena.html', {'deena' : deena})

def denise(request):
    return render(request, 'blogs/denise.html', {'denise' : denise})

def sandra(request):
    return render(request, 'blogs/sandra.html', {'sandra' : sandra})

def robin(request):
    return render(request, 'blogs/robin.html', {'robin' : robin})