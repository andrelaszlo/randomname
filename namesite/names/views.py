# Create your views here.

from django.shortcuts import render_to_response
from random_name.names import generate_name

from random import randint

def main(request):
    if randint(0,1) == 0:
        return male(request)
    else:
        return female(request)

def namepage(first):
    last = generate_name('last', 4)
    return render_to_response('names/main.html', {'first': first,
                                                  'last': last,
                                                  'url': first + "%20" + last})

def male(request):
    first = generate_name('male')
    return namepage(first)

def female(request):
    first = generate_name('female')
    return namepage(first)

def share(request, name=''):
    return render_to_response('names/share.html', {'name': name})

def comments(request):
    return render_to_response('names/comments.html', {})

def about(request):
    return render_to_response('names/about.html', {})
