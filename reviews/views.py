from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib import messages
from reviews.models import Review
from reviews.forms import ReviewForm
from static_strings.models import MailToString


# def reviews(request):
#     reviews = Review.objects.filter(published=True)
#     form = ReviewForm()

#     context = {
#         'reviews': reviews,
#         'form': form,
#     }

#     return render(request, 'reviews/reviews.html', context)


def reviews(request):
    reviews = Review.objects.filter(published=True)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                review = Review.objects.create(
                    email = form.cleaned_data['email'],
                    name = form.cleaned_data['name'],
                    text = form.cleaned_data['text'],
                    image = form.cleaned_data['image'],
                )

                current_site = get_current_site(request)
                mail_subject = 'Новый отзыв на сайте: ' + current_site.domain
                message = render_to_string('reviews/new_review_message.html', {
                    'domain': current_site.domain,
                    'review': review,
                })
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()

                messages.success(request, '<strong>Ваш отзыв отправлен!</strong> После модерации он появится на сайте.', extra_tags='success')
                form = ReviewForm()
            except:
                messages.success(request, '<strong>При отправке произошла ошибка!</strong> Повторите попытку позже.', extra_tags='danger')
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)