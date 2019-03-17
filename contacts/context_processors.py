from contacts.models import Phone


def getting_phone(request):
    phone = Phone.objects.first()

    context = {
        'phone': phone,
    }

    return context