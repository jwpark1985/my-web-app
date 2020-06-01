from django.shortcuts import render
from .models import Document, Source

# Create your views here.
def document_list(request):
    source = Source.objects.get(data_source='NC')
    docs = Document.objects.filter(data_source=source)
    return render(request, 'data/doc_list.html', {'docs': docs})
