from django.shortcuts import render
from seminars.models import Seminar, UpcomingSeminar


def all_seminars(request):
    all_seminars = Seminar.objects.all()

    context = {
        'all_seminars': all_seminars,
    }

    return render(request, 'seminars/all_seminars.html', context)


def upcoming_seminars(request):
    upcoming_seminars = UpcomingSeminar.objects.all()

    context = {
        'upcoming_seminars': upcoming_seminars,
    }

    return render(request, 'seminars/upcoming_seminars.html', context)


def seminar_detail(request, seminar_id):
    seminar = Seminar.objects.get(id=int(seminar_id))

    context = {
        'seminar': seminar,
    }

    return render(request, 'seminars/seminar_detail.html', context)