from django.http.response import HttpResponse
from django.shortcuts import render
from .documents import searchDocument

# Create your views here.

def home (request):
    q = request.GET.get('q')
    title = request.GET.get('title')
    author = request.GET.get('author')
    if q:
        search = searchDocument.search().query('match', description_abstract=q)
        total = search.count()
        search = search[0:total]
        results = search.execute()
        amount = results.hits.total.value
    elif title:
        search = searchDocument.search().query('match', title=title)
        total = search.count()
        search = search[0:total]
        results = search.execute()
        amount = results.hits.total.value
    elif author:
       search = searchDocument.search().query('match', contributor_author=author)
       total = search.count()
       search = search[0:total]
       results = search.execute()
       amount = results.hits.total.value
    else:
        search = ''

    return render(request, 'home/index.html', {'search': search, 'total': total,})