# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from settings import *
from models import *
from forms import *
from imdb import IMDb
import os

def scanpath(path):
    if os.path.exists():
        ListOfMovies=os.path.listdir()
        ia = imdb.IMDb()
        for item in ListOfMovies:
            FirstResult = ia.search_movie(item)[0]
            ia.update(FirstResult)
            NewMovie = models.Movie(title = FirstResult['title'], runtime = FirstResult['runtime'], rating = FirstResult['rating']) 
        
    else :
        return 0;
def getscanpath():

    if request.method != 'POST':
        form = forms.MoviePathForm()
    
    else:
        data = request.POST.copy()
        form = forms.MoviePathForm(data)
        scanpath(form.cleaned_data['path'])    
        
    return render_to_response('MoviePath.html',locals())
        
