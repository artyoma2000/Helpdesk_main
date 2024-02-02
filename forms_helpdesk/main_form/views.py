from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

def news_home(request):
    return render(request, 'main_form/news_home.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {

        'form': form,
        'error': error

    }

    return render(request, 'main_form/create.html', data)
