from django.shortcuts import render
from contacts.models import Contact


def contacts(request):
    contact = Contact.objects.first()

    context = {
        'contact': contact,
    }

    return render(request, 'contacts/contacts.html', context)