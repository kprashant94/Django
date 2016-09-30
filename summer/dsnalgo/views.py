from django.shortcuts import render, get_object_or_404
from . models import Article, SubArticle

def dsnalgo(request):
    all_articles = Article.objects.all()
    context = {'all_articles':all_articles}
    return render(request, 'dsnalgo/article_list.html', context)

def article_detail(request,article_id):
    #article = Article.object.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    all_articles = Article.objects.all()
    context = {'article':article, 'all_articles':all_articles}
    return render(request, 'dsnalgo/article_detail.html', context)

def sub_article_detail(request, article_id, sub_article_id):
    sub_article = get_object_or_404(SubArticle,pk=sub_article_id)
    article = get_object_or_404(Article, pk=article_id)
    all_articles = Article.objects.all()
    context = {'article': article, 'all_articles': all_articles, 'sub_article':sub_article}
    return render(request,'dsnalgo/sub_article_detail.html',context)


