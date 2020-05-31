from django.shortcuts import render

# Create your views here.
def document_list(request):
    return render(request, 'data/document_list.html', {})
