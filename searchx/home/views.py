from home.models import History, Resultsave, Searchsave
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .documents import searchDocument
#from .filters import SearchFilter
from elasticsearch import Elasticsearch 
import operator
from functools import reduce
from elasticsearch_dsl import search
from elasticsearch_dsl.query import Q
from django.core.paginator import (
    Paginator, Page, EmptyPage, PageNotAnInteger,
)
from django.utils.functional import LazyObject
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


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

            reduce(operator.iand, queries)

        countval1 = Advsearch.count()
        Advsearch = Advsearch[0:countval1]
        results = Advsearch.execute() 
        
    except Exception as c:
        Advsearch = ''
        countval1 = 0

    q = request.GET.get('q','')
    q = q.replace('<','')
    q = q.replace('>','')


    try:
        if (q != '' and q is not None) :
            search = searchDocument.search().query("multi_match", query=q, 
            fields=['title', 'description_abstract', 'contributor_author'])
            search = search.highlight_options(order='description_abstract')
            search = search.highlight('title')
            #blogs = search.objects.filter(title__icontains=q).order_by('-created')

        countval = search.count()
        search = search[0:countval]
        search = search.highlight('description_abstract')
        results = search.execute()
        
    except:
        search = ''
        results = ''
        countval = countval1
        blogs = '' 

    paginator = Paginator(SearchResults(search),10)
    page_number = request.GET.get("page")
    


    try:
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except Exception as c:
        page = ''

    
    context = {
            'search':page,
            'Advsearch':Advsearch,
            'countval':countval,
            'countval1':countval1,
            'results': results,
            'q':q,
            #'blogs': blogs
            }
    if request.user.is_authenticated:
        term = History.objects.create(
            search_term = q,
            username = User.get_username(request.user)
            )
        term.save() 
    else:
        term = History.objects.create(
            search_term = q,
            username = 'AnonymousUser'
            )
        term.save() 

    if request.user.is_authenticated:
        if request.method == 'POST':
            u_form = Searchsave(request.POST)
            if u_form.is_valid():
                u_form.save()

    return render(request, 'home/index.html',context)

class SearchResults(LazyObject):
    def __init__(self, search_object):
        self._wrapped = search_object

    def __len__(self):
        return self._wrapped.count()

    def __getitem__(self, index):
        search_results = self._wrapped[index]
        if isinstance(index, slice):
            search_results = list(search_results)
        return search_results

def favorite_add(request,title):
    #a = Resultsave.objects.get(username=User.get_username(request.user),title=title)
    if Resultsave.objects.filter(username=User.get_username(request.user),title=title).exists():
        r = Resultsave.objects.filter(username=User.get_username(request.user),title=title).delete()
        saved = False
    else:
        r = Resultsave.objects.create(username=User.get_username(request.user),title=title)
        r.save()
        saved = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'],saved)

def adsearch(request):

    searchixs="add"
    countval=0
    context = {
            'searchixs':searchixs,
            'countval':countval
            

            }
    return render(request, 'search/adsearch.html',context,countval)



    