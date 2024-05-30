from django.shortcuts import render



def index(request):
    return render(request, "main/index.html")

def resume(request):
    data = {
        'title': 'My career',
        'values': ['some','121','hello'],
    }
    return render(request,"main/resume.html", data)


def contacts(request):
    return render(request,"main/contacts.html")