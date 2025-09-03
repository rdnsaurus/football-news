from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406361712',
        'name': 'Muhathir M. Radian Oki',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)