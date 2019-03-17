from django.shortcuts import render
from documents.models import Document


def all_documents(request):
    all_documents = Document.objects.all()

    context = {
        'all_documents': all_documents,
    }

    return render(request, 'documents/all_documents.html', context)