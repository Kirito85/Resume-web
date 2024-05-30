from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView,DeleteView


def main_news(request):
    newws = Artiles.objects.order_by("-date")[:5]
    return render(request, "news/main_news.html", {'news': newws})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = "news/deteils_view.html"
    context_object_name =  'article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    form_class= ArtilesForm
class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = "/news"
    template_name = 'news/news_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
        else:
            error = "Form isn`t correct"

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, "news/create.html", data)