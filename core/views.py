from django.shortcuts import render

#for practice
def home(request):
    context = {
        'name': 'Vinod'
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')