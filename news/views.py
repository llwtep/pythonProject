from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(request):
    news=Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})

class NewsDetailsView(DetailView):
    model=Articles
    template_name = 'news/detail_news.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model=Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model=Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/'

def create(request):
    error = ''
    if request.method=='POST':
        form = ArticlesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='NO correct data'


    form=ArticlesForm()
    data={
        'form':form,
        'error':error
    }
    return render(request, 'news/create.html', data)
