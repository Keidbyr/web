from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from articles.models import Article
from . import forms
from django.http import HttpResponse


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles': articles})


def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article_item.html', {'article': article})


@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.CreateArticle()
    return render(request, 'article_form.html', {'form': form})


@login_required(login_url='accounts:login')
def article_update(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.author.id:
        form = forms.CreateArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        else:
            form = forms.CreateArticle(instance=article)
        return render(request, 'article_form.html', {'form': form})


@login_required(login_url='accounts:login')
def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.user.id:
        if request.method == 'POST':
            article.delete()
            return redirect('homepage')
        return render(request, 'article_delete.html', {'article': article})
    return HttpResponse('401 Unathorized', status=401)
