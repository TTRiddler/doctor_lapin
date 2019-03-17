from django.shortcuts import render
from seminars.models import UpcomingSeminar
from articles.models import Article
from contacts.models import Contact
from reviews.models import Review


def index(request):
    upcoming_seminars = UpcomingSeminar.objects.all()

    latest_articles = Article.objects.all()
    if len(latest_articles) > 3:
        latest_articles = latest_articles[len(latest_articles)-3:]

    latest_reviews = Review.objects.all()
    if len(latest_reviews) > 3:
        latest_reviews = latest_reviews[len(latest_reviews)-3:]

    contact = Contact.objects.first()

    context = {
        'upcoming_seminars': upcoming_seminars,
        'latest_articles': latest_articles,
        'latest_reviews': latest_reviews,
        'contact': contact,
    }

    return render(request, 'landing/index.html', context)