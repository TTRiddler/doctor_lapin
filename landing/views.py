from django.shortcuts import render
from seminars.models import UpcomingSeminar, Seminar
from articles.models import Article
from contacts.models import Contact
from reviews.models import Review
from static_elements.models import Quote, SomeInfo


def index(request):
    upcoming_seminars = UpcomingSeminar.objects.all()

    popular_seminars = Seminar.objects.filter(in_index=True)
    if len(popular_seminars) > 6:
        popular_seminars = popular_seminars[len(popular_seminars)-6:]

    latest_articles = Article.objects.all()
    if len(latest_articles) > 3:
        latest_articles = latest_articles[len(latest_articles)-3:]

    latest_reviews = Review.objects.all()
    if len(latest_reviews) > 3:
        latest_reviews = latest_reviews[len(latest_reviews)-3:]

    contact = Contact.objects.first()

    quote = Quote.objects.first()
    someinfo = SomeInfo.objects.first()

    context = {
        'upcoming_seminars': upcoming_seminars,
        'latest_articles': latest_articles,
        'latest_reviews': latest_reviews,
        'contact': contact,
        'popular_seminars': popular_seminars,
        'quote': quote,
        'someinfo': someinfo,
    }

    return render(request, 'landing/index.html', context)