from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'variable1': "Raman1",
        'variable2': "Raman2"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is our homepage")

def about(request):
    return render(request, 'about.html')
def backend(request):
    return render(request, 'backend.html')
def frontend(request):
    return render(request, 'frontend.html')
def databases(request):
    return render(request, 'databases.html')
def contact(request):
    return render(request, 'contact.html')

