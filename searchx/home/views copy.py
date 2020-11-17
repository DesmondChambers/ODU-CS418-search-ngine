from django.http.response import HttpResponse
from django.shortcuts import render
from .documents import searchDocument
#from .filters import SearchFilter
from elasticsearch import Elasticsearch 
import operator
from functools import reduce
from elasticsearch_dsl import search
from elasticsearch_dsl.query import Q
from django.core.paginator import Paginator, Page

# Create your views here.

def home(request):
    client = Elasticsearch()
    title = request.GET.get('title')
    author = request.GET.get('author')
    paginate_by = 10

    try:
        queries = []

        if title:
            queries.append(Q(
                'match',
                title=title,
            ))
        if author:
            queries.append(Q(
                'match',
                contributor_author=author,
            ))

        Advsearch = searchDocument.search().query(
            reduce(operator.iand, queries))

        countval1 = Advsearch.count()
        Advsearch = Advsearch[0:countval1]
        results = Advsearch.execute() 
        
    except Exception as c:
        Advsearch = ''
        countval1 = 0

    q = request.GET.get('q')


    try:
        if (q != '' and q is not None) :
            search = searchDocument.search().query("multi_match", query=q, 
            fields=['title', 'description_abstract', 'contributor_author'])
            search = search.highlight_options(order='description_abstract')
            search = search.highlight('title')

        countval = search.count()
        search = search[0:countval]
        search = search.highlight('description_abstract')
        results = search.execute()
        
    except:
        search = ''
        results = ''
        countval = countval1  

    
    context = {
            'search':search,
            'Advsearch':Advsearch,
            'countval':countval,
            'countval1':countval1,
            'results': results
            }

    return render(request, 'home/index.html',context)