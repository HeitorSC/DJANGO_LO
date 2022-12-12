from django.shortcuts import render


# Create your views here.
def my_home(request):
    return render(request, 'global/home.html', status=201, context={
        'name': '<br/>Heitor'
    })
