from django.shortcuts import render



def index(request):
    data = {
        'title': 'About me',
    }
    return render(request, "main/resume.html",data)

def resume(request):
    data = {
        'title': 'About me',
        'values': ['some','121','hello'],
    }
    return render(request,"main/resume.html", data)


def contacts(request):
    return render(request,"main/contacts.html")