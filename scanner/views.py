# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from settings import *
from daedra.scanner.models import *
from forms import *
from imdb import IMDb
import os

def scanpath(path):
    if os.path.exists(path):
        ListOfMovies=os.listdir(path)
        print ListOfMovies
        ia = IMDb()
        for item in ListOfMovies:
            try:
                query = os.path.splitext(item)[0]
                FirstResult = ia.search_movie(query)[0]
                ia.update(FirstResult)
                try:
                    exists = Film.objects.get(title = FirstResult['title'])
                except:
                    exists = None   
                if(exists is None):   
                    NewMovie = Film(title = "")
                    try:
                        NewMovie.title = FirstResult['title']
                    except:
                        pass
                    try:
                        NewMovie.rating = FirstResult['rating']
                    except:
                        pass
                    try:
                        NewMovie.runtime = FirstResult['runtime'][0]
                    except:
                        pass
                    try:
                        NewMovie.summary = FirstResult['plot'][0]
                    except:
                        pass
                    try:
                        NewMovie.coverurl = FirstResult['cover url']
                        os.chdir(MEDIA_ROOT)
                        os.system("wget " + NewMovie.coverurl)
                        os.chdir(path)
                    except:
                        pass
                    try:
                        NewMovie.genre = ",".join(FirstResult['genre'])
                    except:
                        pass
                    try:
                        NewMovie.director = FirstResult['director'][0]
                    except:
                        pass
                    print NewMovie    
                    NewMovie.save()
            except:
                pass                
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
        
