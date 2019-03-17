from django.shortcuts import render, redirect
from reviews.models import Review
from reviews.forms import ReviewForm


# def reviews(request):
#     reviews = Review.objects.all()

#     context = {
#         'reviews': reviews,
#     }

#     return render(request, 'reviews/reviews.html', context)


def reviews(request):
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = Review.objects.create(
                email = form.cleaned_data['email'],
                name = form.cleaned_data['name'],
                text = form.cleaned_data['text'],
                image = form.cleaned_data['image'],
            )
        return redirect('reviews')
    else:    
        form = ReviewForm()
    
    context = {
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)