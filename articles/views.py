from django.shortcuts import render
from articles.models import Article


def all_articles(request):
    all_articles = Article.objects.filter(published=True)

    context = {
        'all_articles': all_articles,
    }

    return render(request, 'articles/all_articles.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(id=int(article_id))

    context = {
        'article': article,
    }

    return render(request, 'articles/article_detail.html', context)